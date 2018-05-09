import os
import os.path as osp
import matplotlib.pylab as pl
import numpy as np
from pathlib import Path
from PIL import Image

home_dir = Path.home()
work_dir = osp.join(home_dir, 'work', 'work-py-tryout')
print("work_dir: '{}'".format(work_dir))
if not osp.exists(work_dir):
    os.makedirs(work_dir)


def plot_image(_img: np.array, _img_file: str):
    _a = (_img * 256).astype(np.uint8)
    print(_a)
    _i = Image.fromarray(_a, mode='RGBA')
    _i.save(_img_file, format='PNG')


img_file = "res/img01.png"
print("reading {}".format(img_file))
img: np.array = pl.imread(img_file)

h = img.shape[0]
w = img.shape[1]
print("img w:{} h:{}".format(w, h))

transp = np.empty([h, w], dtype=np.float32)
for i in range(h):
    for j in range(w):
        transp[i, j] = j / w

# Add transparency
img1 = np.insert(img, 3, transp, axis=2)

out_file = osp.join(work_dir, "out9.png")
plot_image(img1, out_file)

print("saved image to {}".format(out_file))
