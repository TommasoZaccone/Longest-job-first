#!/usr/bin/env python

import matplotlib.pyplot as plt
import csv

x = []
y = []
ylabel = 'error'
with open("results/out.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(row[0])
        y.append(row[1])

    ylabel = y[0]
    x = x[1:]
    y = y[1:]

plt.plot(x,y)
plt.ylabel(ylabel)
plt.show()


