#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
import numpy

import data_utils

if len(sys.argv)<3:
    print("arguments:[bins] [files]")
    exit(1)

bins = int(sys.argv[1])
files = sys.argv[2:]

labels,vecs = data_utils.load_csv(files)

for l,x in zip(labels,vecs):
    print("label: "+l)
    print("sample size: "+str(len(x)))
    print("sample mean: "+str(numpy.mean(x)))

    plt.hist(x,bins=bins,normed=True,histtype='step',label=l)

plt.legend()
plt.show()


