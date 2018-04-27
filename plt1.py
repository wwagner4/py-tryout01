import numpy as np
import matplotlib.pyplot as plt
import os

wd = "/Users/wwagner4/work/work-vsoc-ga-2018/"
imgd = wd + "py-img/"
if not os.path.exists(imgd):
    os.makedirs(imgd)


def plot(_nr: str, _sp_cfg: int):
    train = np.genfromtxt(wd + "trainGaKicks01/bob{0}/trainGaKicks01-bob{0}-data.csv".format(_nr),
                          delimiter=';', skip_header=1)[:, 2:4]
    print("nr sp_cfg {} {}".format(_nr, _sp_cfg))

    sp = fig.add_subplot(_sp_cfg)

    x = train[:, 0:1]
    y = train[:, 1:2]
    sp.plot(x, y, linewidth=0.5)


fig = plt.figure()

cfgs = [('003', 221), ('004', 222), ('005', 223), ('006', 224)]

for (nr, sp_cfg) in cfgs:
    plot(nr, sp_cfg)


fig.savefig(imgd + "t3.png", dpi=300, papertype='a3')
plt.show()
