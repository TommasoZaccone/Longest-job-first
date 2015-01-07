#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys

import data_utils


if len(sys.argv)<2:
    print("arguments:[files]")
    exit(1)

files = sys.argv[1:]

labels,vecs = data_utils.load_csv_intervals(files)

nvecs = []

for v in vecs:
    nvec = []
    tot = 0
    for k in v:
        tot += k
    for k in v:
        nvec.append(k/tot)
    nvecs.append(nvec)


for l,v in zip(labels,nvecs):
    mean = 0
    for i,k in enumerate(v):
        mean += i*k
    print(l+": mean="+str(mean))

    plt.plot(v,marker="o",linestyle="dashed",label=l)

plt.legend()
plt.show()


