#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy
import re
import glob

import data_utils

fifo = glob.glob("results/FIFO-*.csv")
ljf = glob.glob("results/LJF-*.csv")

iter = [fifo,ljf]

for i in iter:
    labels,vecs = data_utils.load_csv(i)
    means = [numpy.mean(v) for v in vecs]
    labels = [l for m,l in sorted(zip(means,labels))]
    means.sort()
    del vecs

    x = []
    y = []
    for label,m in zip(labels,means):
        params = re.match("(.*)-([0-9]+(?:\.[0-9]+)*)-([0-9]+(?:\.[0-9]+)*)",label)
        policy = params.group(1)
        iaM = float(params.group(2))
        sMean = float(params.group(3))

        y.append(m)
        x.append(iaM)

    plt.plot(x,y,label=policy)



sM = 4

x = []
y = []

for i in numpy.linspace(sM,12,num=1000,endpoint=False):
    y.append(1/(1/sM-1/i))
    x.append(i)

plt.plot(x,y,label="theorical")

plt.legend()
plt.xlabel("mean interarrival time")
plt.ylabel("mean response time")
plt.show()



