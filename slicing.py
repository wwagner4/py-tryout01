import numpy as np

a = np.array([
    np.arange(1, 5),
    np.arange(1, 5),
    np.arange(1, 5),
    np.arange(1, 5),
    np.arange(1, 5),
    np.arange(1, 5)
])

x = a[:, :-1]
y = a[:, -1:]

print("a {}".format(a.shape))
print("x {}".format(x.shape))
print("y {}".format(y.shape))
print("x {}".format(x))
print("y {}".format(y))
