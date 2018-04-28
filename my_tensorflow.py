import tensorflow as tf
import numpy as np
import os.path as osp
import pathlib as pl
import time as ti

from tensorflow import Variable

home_dir = pl.Path.home()
work_dir = osp.join(home_dir, "work/work-greenscreen")


def nd_arrays():
    m1 = [[1, 2, 3], [2, 3, 5]]

    m2 = np.array([[1, 2, 3], [2, 3, 4]])

    m3 = tf.constant([[1.4, 2, 3], [2, 3, 4], [8, 1, 2]], name="ww99")

    print("m1 ?? %s" % m1)
    print("m2 %s %s" % (m2.shape, m2))
    print("m3 %s %s" % (m3.shape, m3))

    t1 = tf.convert_to_tensor(m1, name="ww01")
    t2 = tf.convert_to_tensor(m2, name="ww02")
    t3 = tf.convert_to_tensor(m3, name="ww03")

    print("t1 %s %s" % (t1.shape, t1))
    print("t2 %s %s" % (t2.shape, t2))
    print("t3 %s %s" % (t3.shape, t3))


def flow():
    t4 = tf.ones([2, 4], name="z")
    t5 = tf.negative(t4, name="n")
    with tf.Session() as sess:
        result = sess.run(t5)
        print("result %s" % result)


def variables1():
    with tf.Session() as sess:  # Create a session
        raw_data = [1, 4, 17, 22, 6, 3, 4, 23, 2, 3, 10, 5, 6, 7]
        spike = tf.Variable(False)
        spike.initializer.run(session=sess)  # create and initialize a tf variable

        print("spike (is bool_ref:%s) (size is 0:%s) %s %a"
              % (spike.dtype == "bool_ref", len(spike.shape) == 0, spike.shape, spike))

        for i in range(1, len(raw_data)):
            if raw_data[i] - raw_data[i - 1] > 4:
                updater = tf.assign(spike, True)  # update the tf variable
                res = updater.eval(session=sess)
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))
            else:
                updater = tf.assign(spike, False)  # update the tf variable
                res = updater.eval(session=sess)
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))


def variables_s():
    with tf.Session() as sess:  # Create a session
        raw_data = [1, 4, 17, 22, 6, 3, 4, 23, 2, 3, 10, 5, 6, 7]
        spikes_init = np.full((len(raw_data)), False)
        print("spikes_init:%s" % spikes_init)
        spikes = tf.Variable(spikes_init, name="sps")
        spikes.initializer.run()  # create and initialize a tf variable

        # Must be initialized after variables are initialized in the session
        # Saves all tf variables that where initialized before the saver
        # is initialized
        saver = tf.train.Saver()

        print("spike (is bool_ref:%s) (size is 0:%s) %s %a"
              % (spikes.dtype == "bool_ref", len(spikes.shape) == 0, spikes.shape, spikes))

        for i in range(1, len(raw_data)):
            if raw_data[i] - raw_data[i - 1] > 4:
                updater = tf.assign(spikes[i], True, name='up')  # update the tf variable
                res = updater.eval()
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))
            else:
                updater = tf.assign(spikes[i], False, name='up')  # update the tf variable
                res = updater.eval()
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))

        pa = saver.save(sess, osp.join(work_dir, "v001.ckpt"))
        print("saved to '%s'" % pa)


def variables_r():
    with tf.Session() as sess:
        spikes = tf.Variable(np.full(14, False), name="sps")  # size must be the same as the stored variable
        saver = tf.train.Saver()
        up = tf.Variable(True, name="up")
        up.initializer.run()
        saver.restore(sess, osp.join(work_dir, "v001.ckpt"))

        print("resored sp %s" % spikes.eval())
        print("resored up %s" % up.eval())


def moving_average():
    with tf.Session() as sess:
        raw_data = np.random.normal(10, 1, size=50)
        print("raw_data: %s" % raw_data)

        alpha = tf.constant(0.1)  # must not necessarily be a tensor constant. Can be a float
        curr_val = tf.placeholder(tf.float32)

        avg: Variable = tf.Variable(0.0)

        sess.run(tf.global_variables_initializer())  # initialize all variables and placeholders

        # define the operation
        mov_avg_op = alpha * curr_val + (1 - alpha) * avg

        # define summaries and writer for TensorBoard
        avg_sum = tf.summary.scalar('running_average', mov_avg_op)
        writer = tf.summary.FileWriter(osp.join(work_dir, "logs"))

        for i, val in enumerate(raw_data):
            (avg_str, new_avg) = sess.run([avg_sum, mov_avg_op], feed_dict={curr_val: val})
            print("new_avg %s %5.3f" % (type(new_avg), new_avg))
            sess.run(tf.assign(avg, new_avg))
            writer.add_summary(avg_str, i)
            print("%5.2f %5.2f" % (val, new_avg))
            ti.sleep(0.05)


moving_average()
