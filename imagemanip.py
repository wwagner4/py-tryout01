import os
import os.path as osp
import matplotlib.pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

home_dir = Path.home()
work_dir = osp.join(home_dir, 'work', 'work-py-tryout')
print("work_dir: '{}'".format(work_dir))
if not osp.exists(work_dir):
    os.makedirs(work_dir)


def plot_image(_img: np.array, img_file: str):
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    plt.axis('off')
    plt.imshow(_img)
    plt.savefig(img_file)


img_file = "res/img01.png"
print("reading {}".format(img_file))
img: np.array = pl.imread(img_file)

print("img {}".format(img.shape))

# Add transparency
img1 = np.insert(img, 3, 0.2, axis=2)

out_file = osp.join(work_dir, "out6.png")
plot_image(img1, out_file)

print("saved image to {}".format(out_file))
