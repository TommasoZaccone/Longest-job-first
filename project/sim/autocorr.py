#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.mlab as m
import sys
import numpy
import random

import data_utils

if len(sys.argv)!=3:
    print("arguments:[file] [k]")
    exit(1)

f = sys.argv[1]
k = int(sys.argv[2])

labels,vecs = data_utils.load_csv([f])
label = labels[0]
vec = vecs[0]
x = []
p = 1/(2**k)
for v in vec:
    if(random.random() < p):
        x.append(v)

conf = m.prctile(x,97.5)
print("label: "+label)
print("sample size: "+str(len(x)))
print("sample mean: "+str(numpy.mean(x)))
print("97.5%: "+str(conf))

line = conf/numpy.sqrt(len(x))
plt.axhline(line)
plt.axhline(-line)
plt.acorr(x,label=label)
plt.legend()
plt.show()


