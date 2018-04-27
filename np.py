import numpy as np

print("numpy version {}".format(np.version.short_version))
print("pi:{:.50f}".format(np.pi))
print("pi type:{}".format(type(np.pi)))

array1 = np.array([1, 2, 3, 4, 5])
print("array1 type:{}".format(type(array1)))
print("array1.all {}".format(array1.all()))

array2 = np.zeros([2, 4, 10])
print("array2:{}".format(array2))

print()

array3 = np.arange(1, 10, 1.1)
print("array3:{}".format(array3))

array4 = np.array([[1, 2], [5, 2]])
print("array4:{}".format(array4))
print("array2 ndim:{}".format(array2.ndim))
print("array4 ndim:{}".format(array4.ndim))
print("array2 shape:{}".format(array2.shape))
print("array4 shape:{}".format(array4.shape))

print("array4 inv:{}".format(np.linalg.inv(array4)))
print("- - - - - - - - - - - - - - - - - - - - - - - -")

