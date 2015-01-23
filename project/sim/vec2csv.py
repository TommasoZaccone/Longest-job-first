#!/usr/bin/env python

import sys
import os
import sh
import re
import glob


if len(sys.argv)<2:
    print("arguments: [variabls]")
    exit(1)

variables = sys.argv[1:]

os.chdir(os.path.dirname(sys.argv[0]))

vecs = [v for v in os.listdir("results") if re.match(".*\-0.vec$",v)]

#capture float: ([0-9]+(?:\.[0-9]+)*)
r = re.compile('^((.*)-"(.*)"-(.*))-0.vec$')
    
os.chdir("results")
for v in vecs:
    captures = r.match(v)

    sourceglob = captures.group(1)+"-*.vec"
    sources = glob.glob(sourceglob)
    
    dist = captures.group(2)
    policy = captures.group(3)
    params = captures.group(4)
    

    for v in variables:
        name = v+'-'+dist+'-'+policy+'-'+params+'.csv'

        sh.scavetool("v","-p",v+":vector","-O",name,"-F","csv",sources)
        print(name)


