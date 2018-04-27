import numpy as np
import matplotlib.pyplot as plt
import os

wd = "/Users/wwagner4/work/work-vsoc-ga-2018/"
imgd = wd + "py-img/"
if not os.path.exists(imgd):
    os.makedirs(imgd)

fig = plt.figure()
sp = fig.add_subplot(111)


def plot(_nr: str):
    train = np.genfromtxt(wd + "trainGaKicks01/bob{0}/trainGaKicks01-bob{0}-data.csv".format(_nr),
                          delimiter=';', skip_header=1)[:, 2:4]
    print("nr {}".format(_nr))

    x = train[:, 0:1]
    y = train[:, 1:2]

    plt.plot(x, y, linewidth=0.5, label=_nr)


cfgs = ['003', '004', '005', '006']

for nr in cfgs:
    plot(nr)

plt.legend()

fig.savefig(imgd + "t4.png", dpi=300, papertype='a4')
plt.show()
