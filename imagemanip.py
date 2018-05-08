import os.path as osp
import matplotlib.pylab as pl
import numpy as np
import matplotlib.pyplot as plt

workdir = "/Users/wwagner4/work/work-greenscreen"

img_file = "res/img01.png"
print("reading {}".format(img_file))
img: np.array = pl.imread(img_file)

print("img {}".format(img.shape))

# Add transparency 0.1
img1 = np.insert(img, 3, 0.1, axis=2)

plt.imshow(img1)

out_file = osp.join(workdir, "out2.png")
plt.savefig(out_file)
print("saved image to {}".format(out_file))
