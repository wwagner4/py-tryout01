import numpy as np
import matplotlib.pyplot as plt

x_train = np.linspace(0, 100, 100)
y_train = 2.0 * x_train + np.random.randn(x_train.shape[0]) * 10
# print("y_train %s %s" % (type(y_train), y_train))
# print("x_train %s" % x_train)

plt.scatter(x_train, y_train)
plt.show()
