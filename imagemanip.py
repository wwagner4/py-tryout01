import os
import os.path as osp
import matplotlib.pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import random as ran
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

h = img.shape[0]
w = img.shape[1]
print("img w:{} h:{}".format(w, h))

transp = np.empty([h, w], dtype=np.float32)
for i in range(h):
    for j in range(w):
        transp[i, j] = i / h + ran.uniform(0.0, 0.1)
        
# Add transparency
img1 = np.insert(img, 3, transp, axis=2)

out_file = osp.join(work_dir, "out7.png")
plot_image(img1, out_file)

print("saved image to {}".format(out_file))
