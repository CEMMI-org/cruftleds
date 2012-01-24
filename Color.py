#!/usr/bin/env python

import sys;
from time import sleep;
from numpy import *;
from scipy.signal import correlate2d;
from teh_display import *;

N = 50;
M = 24;
data = zeros([3*N,M]);

rgb = array([ float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])]);
for i in range(0,N):
  for j in range(0,M):
    for k in range(0,3):
	data[3*i+k,j] = rgb[k];

teh_display(data);

if len(sys.argv) == 5:
  sleep(float(sys.argv[1]))

