#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
import numpy

import data_utils

if len(sys.argv)<3:
    print("arguments:[bins] [files]")
    exit(1)

bins = float(sys.argv[1])
files = sys.argv[2:]

labels,vecs = data_utils.load_csv(files)

for l,x in zip(labels,vecs):
    x.sort()
    print("label: "+l)
    print("sample size: "+str(len(x)))
    print("sample mean: "+str(numpy.mean(x)))
    print("sample median: "+str(numpy.median(x)))
    print("sample variance: "+str(numpy.var(x)))
    print("sample coefficient of variation: "+str(numpy.sqrt(numpy.var(x))/numpy.mean(x)))
    print("sample percentiles [25%,50%,75%,95%,99%]: "+str(numpy.percentile(x, [25,50,75,95,99])))
    print()

    b = int(numpy.max(x)*10/bins)
    plt.hist(x,bins=b,normed=True,histtype='step',label=l)

plt.legend()
plt.show()


