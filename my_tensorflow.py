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
    t4 = tf.zeros([2, 4], name="z")
    t5 = tf.negative(t4, name="n") + 100 * 0.0002345
    print("t4 %s" % t5)


flow()
