#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
import numpy

import data_utils

if len(sys.argv)<2:
    print("arguments:[files]")
    exit(1)

files = sys.argv[1:]

labels,vecs = data_utils.load_csv(files)

for l,k in zip(labels,vecs):
    print("label: "+l)
    print("sample size: "+str(len(k)))
    print("sample mean: "+str(numpy.mean(k)))

    y = [0]
    x = [0]
    N = len(k)
    S = sum(k)
    n = 0
    s = 0
    for i in k:
        n+=1
        s+=i
        x.append(n/N)
        y.append(s/S)

    plt.plot(x,y,label=l)

plt.plot([0,1])

plt.legend()
plt.show()


