#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy
import re
import glob
import sys

import data_utils

if len(sys.argv)<2:
    print("arguments: [variable]")
    exit(1)

variable = sys.argv[1]
files = glob.glob("results/"+variable+"-*.csv")

labels,vecs = data_utils.load_csv(files)
means = [numpy.mean(v) for v in vecs]
labels = [l for m,l in sorted(zip(means,labels))]
means.sort()
del vecs

x = []
y = []
policies = {}
for label,m in zip(labels,means):
    params = re.match("(.*)-(.*)-([0-9]+(?:\.[0-9]+)*)",label)
    variable = params.group(1)
    policy = params.group(2)
    utilization = float(params.group(3))

    if policy in policies:
        policies[policy][0].append(utilization)
        policies[policy][1].append(m)
    else:
        
        policies[policy] = ([utilization],[m])

for k,v in policies.items():
    plt.plot(v[0],v[1],label=k)




x = []
y = []


sMean = 5
for i in numpy.linspace(0,1,num=1000,endpoint=False):
    y.append(sMean/(1-i))
    x.append(i)

plt.plot(x,y,label="theorical")

plt.legend()
plt.xlabel("mean interarrival time")
plt.ylabel("mean response time")
plt.show()



