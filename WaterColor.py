#!/usr/bin/env python



# Arugments:
#
# Duration -- time to run in secs.
# Alpha -- CGL parameter.
# Beta -- CGL parameter.
# Speed -- Larger means faster (1 is reasonable).
# Scale -- Larger means smoother (1 is reasonable). 
# 
#
# Then either:
#
# nothing: use MATLAB colormap.
#
# R -- Red 
# G -- Green
# B -- Blue for solid colormap (default is Matlab).
#
# Or:
# omega -- Speed to rotate in hue / saturation.

import sys;
from numpy import *;
from scipy.signal import correlate2d;
from teh_display import *;

if len(sys.argv) < 2:
   duration = 10;
else:
   duration = float(sys.argv[1])

if len(sys.argv) < 3:
   alpha = -1;
else:
   alpha = float(sys.argv[2])
   
if len(sys.argv) < 4:
   beta = -1.5;
else:
   beta = float(sys.argv[3])

if len(sys.argv) < 5:
   speed = 1;
else:
   speed = int(sys.argv[4]);

if len(sys.argv) < 6:
   scale = 1;
else:
   scale = float(sys.argv[5]);


N = 50;
M = 24;

dt = 0.005;
t=0;

def dynamics(data,verbose=0):
   global scale;
   dA = correlate2d(data,array([[0,1,0],[1,-4,1],[0,1,0]]),boundary='wrap');
   dA = dA[1:N+1,1:M+1];
   if verbose:
     print(dA[0:5,0:5]);

   data = data + dt*((1+alpha*1j)*scale*dA + data - (1+1j*beta)*data*power(abs(data),2));
#   data[23:25,12:14] = 1;
   return data;
t=0;

import colorsys;
import time;
h = 0;
s = 0;



t0 = time.time();
t = time.time();
from time import sleep as wakeup;

viz = 1j*zeros([3*N,M]);
dataR = 0.01*random.rand(N,M);
dataG = 0.01*random.rand(N,M);
dataB = 0.01*random.rand(N,M);

while t < t0 + duration:
   for i in range(0,10):
      dataR = dynamics(dataR);
      dataG = dynamics(dataG);
      dataB = dynamics(dataB);

   for i in range(0,N):
      for j in range(0,M):
         viz[3*i,j] = (1+real(dataR[i,j]))/2;
         viz[3*i+1,j] = (1+real(dataG[i,j]))/2;
         viz[3*i+2,j] = (1+real(dataB[i,j]))/2;
      
   print(viz[0:3,0])
   teh_display(viz);
   t = time.time();
