#!/usr/bin/env python

import sys
import os
import sh
import re
import glob

os.chdir(os.path.dirname(sys.argv[0]))

vecs = [v for v in os.listdir("results") if re.match(".*\-0.vec$",v)]

r = re.compile('^(General-"(.*)"-([0-9]+(?:\.[0-9]+)*)-([0-9]+(?:\.[0-9]+)*))-0.vec$')
    
os.chdir("results")
for v in vecs:
    params = r.match(v)

    sourceglob = params.group(1)+"-*.vec"
    sources = glob.glob(sourceglob)
    
    policy = params.group(2)
    iaMean = params.group(3)
    sMean = params.group(4)
    

    name = policy+'-'+iaMean+'-'+sMean+'.csv'

    sh.scavetool("v","-p","name(responseT:vector)","-O",name,"-F","csv",sources)
    print(name)


