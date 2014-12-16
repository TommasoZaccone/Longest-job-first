#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
import numpy

import data_utils

if len(sys.argv)<3:
    print("arguments:[bins] [files]")
    exit(1)

files = sys.argv[1:]

labels,vecs = data_utils.load_csv(files)

for l,x in zip(labels,vecs):
    print("label: "+l)
    print("sample size: "+str(len(x)))
    print("sample mean: "+str(numpy.mean(x)))

    y = []
    n = len(x)
    k = 0
    for i in x:
        y.append(k/n)
        k += 1

    plt.plot(x,y,label=l)

plt.legend()
plt.show()


