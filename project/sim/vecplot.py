#!/usr/bin/env python2

"""
//
// Copyright (C) 2009 Institut fuer Telematik, Universitaet Karlsruhe (TH)
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
//
// Authors: Stephan Krause
//
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from optparse import OptionParser 
from matplotlib.font_manager import fontManager, FontProperties
from string import maketrans
import re

def sortedDictValues(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

parser = OptionParser(usage="%prog [options] yvectorname *.vec")
parser.add_option("-i", "--include-only", type="string", dest="include", action="append", help="Include only iterations that match the regexp given by INCLUDE")
parser.add_option("-e", "--exclude", type="string", action="append", help="Exclude iterations that match the regexp given by EXCLUDE")
parser.add_option("-b", "--bucketsize", type="float", default=1.0, dest="bucketsize", help="Size of the buckets for pdf to BUCKETSIZE (default=1.0)")
parser.add_option("-c", "--confidence-intervall", type="float", default=0, dest="ci", help="Plots the confidence intervals with confidence level LEVEL", metavar="LEVEL")
parser.add_option("-l", "--legend-position", type="int", default=0, dest="lpos", help="Position of the legend (default:auto)")
parser.add_option("-t", "--plot-type", type="string", default="pdf", dest="ptype", help="Plot type (pdf,cdf,cdf_inters)")
parser.add_option("-I", "--intersection", type="float", default=1.0, dest="ihint", help="Hint for finding intersection point (only with -t cdf_inters)")
(options, args) = parser.parse_args()

if len(args) < 2: 
    parser.error("Wrong number of options")

incregex = []
if options.include:
    for incopt in options.include:
        incregex.append(re.compile(incopt))

exregex = []
if options.exclude:
    for exopt in options.exclude:
        exregex.append(re.compile(exopt))

if options.ci >=1 or options.ci < 0:
    parser.error("Option 'confidence-intervall': LEVEL must be between 0 and 1")


valuemap = {}

# open all files
for infilename in args[1:]:
    inc = True

    infile = open(infilename, 'r')
    # read vector file
    parseHeader = True
    for line in infile:
        if parseHeader:
            # parse iterationvars
            if line.startswith("attr configname "):
                confname = line[16:].strip()
            if line.startswith("attr iterationvars "):
                vars = line[19:].strip()

                # filter runs: exclude runs that don't match incregex, or that do match exregexp
                for exp in incregex:
                    if not exp.search(vars):
                        inc = False
                for exp in exregex:
                    if exp.search(vars):
                        inc = False
                if not inc:
                    break
                #remove $ and " chars from the string
                vars = vars.translate(maketrans('',''), '$"')

            # find vector number
            if line.startswith("vector"):
                if line.find(args[0]) > -1:
                    vecnum = line.split(" ", 3)[1]
                    vars=confname + "-" + vars;
                    if vars not in valuemap:
                        valuemap[vars]=[]
                    parseHeader = False
        else:
            # header parsing finished, search for the appropriate vectors
            splitline = line.split("\t")
            if splitline[0] == vecnum:
                # get value, and find the bucket for the data
                value = float(splitline[3])
                valuemap[vars].append(value)


if len(valuemap) == 0:
    print "Error: vector \"" + args[0] + "\" not found, or all runs ignored due to the given include and exclude regexp!"
    exit(-1)

# Prepare plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("Time")
ax.set_ylabel(args[0])
ax.grid(True)


def pdf(rundata):
    bins = int(np.max(rundata)/options.bucketsize)
    y,binedges = np.histogram(rundata, normed=True,bins=bins)
    bincenters = 0.5*(binedges[1:]+binedges[:-1])
    return bincenters,y


def cdf(rundata):
    x = np.sort(rundata)
    y = np.arange(len(x))/float(len(x))
    return x,y


colors = ['r','g','b','y','c']
c = 0
f = lambda : None
find_inters = False
inters_hint = 1
if options.ptype == "pdf":
    f = pdf
elif options.ptype == "cdf":
    f = cdf
elif options.ptype == "cdf_inters":
    f = cdf
    if len(valuemap.keys()) == 2:
        find_inters = True
        inters_hint = options.ihint
    else:
        print("Too many runs for cdf_inters")
else:
    print("Plot not supported: "+options.ptype)
    exit(1)

# Go through all runs
for run in sorted(valuemap.keys()):
    rundata = valuemap[run]
    x,y = f(rundata)
    ax.plot(x,y,label=run,color=colors[c])

    ax.axvline(x=np.median(x),ymax = 0.5,color=colors[c],linewidth=1)
    ax.axvline(x=np.percentile(x,95),ymax = 0.95,color=colors[c],linewidth=1)
    
    c = (c+1)%len(colors)

if find_inters:
    x1,y1 = cdf(valuemap.values()[0])
    x2,y2= cdf(valuemap.values()[1])
    f1 = lambda x: np.interp(x,x1,y1)
    f2 = lambda x: np.interp(x,x2,y2)
    xinters = fsolve(lambda x: f1(x)-f2(x),inters_hint)[0]
    yinters = f1(xinters)
    ax.plot([xinters,xinters],[0,yinters],color=colors[c],linestyle='--')
    ax.plot([0,xinters],[yinters,yinters],color=colors[c],linestyle='--')
    print("x:"+str(xinters)+", y:"+str(yinters))


# Display plot
font=FontProperties(size='small')
leg=ax.legend(loc=options.lpos, shadow=True, prop=font)
plt.show()

