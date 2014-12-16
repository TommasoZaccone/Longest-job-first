#!/usr/bin/env python

import csv
import sys
import math
import re

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
        x.sort()
        vecs.append(x)

    return (labels,vecs)

