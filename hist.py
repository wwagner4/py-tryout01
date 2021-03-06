from typing import Union

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from numpy.core.multiarray import ndarray

(fig, ax) = plt.subplots()

# Fixing random state for reproducibility
# np.random.seed(19680801)


# histogram our data with numpy

data = np.random.randn(1000)
print("data shape : {}".format(data.shape))
data1 = [x + 30.0 for x in data]
(n, bins) = np.histogram(data1, 10)

print("n bins {} {}".format(n, bins))

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n


# we need a (numrects x numsides x 2) numpy array for the path helper
# function to build a compound path
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

# get the Path object
barpath = path.Path.make_compound_path_from_polys(XY)

# make a patch out of it
patch = patches.PathPatch(barpath)
ax.add_patch(patch)

# update the view limits
ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

plt.show()