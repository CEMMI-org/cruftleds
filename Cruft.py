#!/usr/bin/env python
# 20 seconds is good

from numpy import *;
import sys;
from time import sleep;
from teh_display import *;

data = genfromtxt('cruft.txt',delimiter=',');
data = (data);
K = shape(data);
print(K)
K = K[0];

N = 50
M = 24;

duration = float(sys.argv[1]);

import time;

t0 = time.time();
t = time.time();
while t < t0 + duration:
   teh_displayi(1-data[0:N,:],colormap.WHITE_COLORMAP);
   time.sleep(0.05);
   sv = data[0,:];
   for j in range(0,K-1):
	data[j,:] = data[j+1,:];
   data[K-1,:] = sv;
   t = time.time();

