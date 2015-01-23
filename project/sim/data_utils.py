#!/usr/bin/env python

import csv
import sys
import math
import re
import numpy


def load_csv(files):
    vecs = []
    labels = []
    for fi in files:
        x = []
        with open(fi) as f:
            label = re.sub("\.csv$","",fi)
            label = re.sub("^.*/","",label)
            labels.append(label)
            reader = csv.reader(f)
            #skip header
            next(reader,None) 
            for row in reader:
                row = row[1:]
                for e in row:
                    try:
                        x.append(float(e))
                    except:
                        pass
        vecs.append(numpy.asarray(x))

    return (labels,vecs)


def load_csv_intervals(files):
    vecs = []
    labels = []
    for fi in files:
        x = []
        with open(fi) as f:
            label = re.sub("\.csv$","",fi)
            label = re.sub("^.*/","",label)
            labels.append(label)
            reader = csv.reader(f)
            #skip header
            header = next(reader,None) 
            for i in range(len(header)-1):
                x.append([])
            for row in reader:
                time = float(row[0])
                row = row[1:]
                for e,s in zip(row,x):
                    try:
                        s.append((time,int(e)))
                    except:
                        pass

        y = {}
        for j in x:
            pn = 0
            pt = 0
            for i in j:
                dt = i[0]-pt
                pt = i[0]
                if pn in y:
                    y[pn]+=dt
                else:
                    y[pn] = dt
                pn = i[1]

        
        l = [e for k,e in y.items()] 
        vecs.append(l)

    return (labels,vecs)

