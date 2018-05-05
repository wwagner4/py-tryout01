import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

learning_rate = 0.1
training_epoches = 2

x_train = np.linspace(-1, 1, 100)
y_train = 2.0 * x_train + np.random.randn(x_train.shape[0]) * 0.3

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
w = tf.Variable(0.0, name="weights")


def model(_x, _w):
    return tf.multiply(_x, _w)


y_model = model(X, w)
cost = tf.square(Y - y_model)
print("cost %s %s" % (type(cost), cost))
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    init = tf.global_variables_initializer()  # init is just an operation
    sess.run(init)
    print("ran 'init'")

    for epoch in range(training_epoches):
        for (x, y) in zip(x_train, y_train):
            score = sess.run(train_op, feed_dict={X: x, Y: y})
            print("w %s" % sess.run(w))

    w_val = sess.run(w)
    print("w_val %s" % w_val)
    y_learned = x_train * w_val

    plt.scatter(x_train, y_train)
    plt.plot(x_train, y_learned, 'r')
    plt.show()
