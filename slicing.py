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

s = np.arange(1, 4)
t = np.arange(9, 10)
rh = np.hstack((s, t))
print("rh {} {}".format(rh.shape, rh))

k = np.array([[[1, 2, 3],
               [1, 2, 3],
               [1, 2, 3]],
              [[1, 2, 3],
               [1, 2, 3],
               [1, 2, 3]]])

print("k = {}".format(k))

l1 = np.insert(k, 3, 10, axis=2)
print("l1 = {}".format(l1))
