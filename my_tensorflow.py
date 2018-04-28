import tensorflow as tf
import numpy as np


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


def variables():
    with tf.Session() as sess:  # Create a session
        raw_data = [1, 4, 17, 22, 6, 3, 4, 23, 2, 3, 10, 5, 6, 7]
        spike = tf.Variable(False)
        sess.run(spike.initializer)  # create and initialize a tf variable

        print("spike (is bool_ref:%s) (size is 0:%s) %s %a"
              % (spike.dtype == "bool_ref", len(spike.shape) == 0, spike.shape, spike))

        for i in range(1, len(raw_data)):
            if raw_data[i] - raw_data[i - 1] > 4:
                updater = tf.assign(spike, True)  # update the tf variable
                res = sess.run(updater)
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))
            else:
                updater = tf.assign(spike, False)  # update the tf variable
                res = sess.run(updater)
                print("%7s %7d %7.2f" % (res, i, raw_data[i]))


variables()
