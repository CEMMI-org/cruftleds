#!/usr/bin/env python


# Arguments:
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

import colorsys
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

if len(sys.argv) < 7:
   CM = colormap.MATLAB_COLORMAP;
   omega = 0;
elif len(sys.argv) == 7:
   omega = float(sys.argv[6]);
   if omega == -1:
      omega = 0;
      CM = 1-colormap.MATLAB_COLORMAP;
elif len(sys.argv) == 9:
   omega = 0;
   CM = colormap.solid_colormap(float(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]));


N = 50;
M = 24;
data = 1j*zeros([N,M]);
field = 0.1*random.randn(N);
dt = 0.002;

# def dynamics(data):
#    dA = 1j*zeros([M+2]);
#    dA[0] = data[M-1];
#    dA[M] = data[0];
#    dA[1:M+1] = data;
#    dA = convolve([1,-2,1],dA);
#    dA = dA[2:M+2];
#    data = data + dt*((1+alpha*1j)*scale*dA + data - (1+1j*beta)*data*power(abs(data),2));
#    return data;
def dynamics(data):
   dA = 1j*zeros([N+2]);
   dA[0] = data[N-1];
   dA[N] = data[0];
   dA[1:N+1] = data;
   dA = convolve([1,-2,1],dA);
   dA = dA[2:N+2];
   data = data + dt*((1+alpha*1j)*scale*dA + data - (1+1j*beta)*data*power(abs(data),2));
   return data;

from time import sleep as wakeup
import time;
h = 0;
s = 0;

t0 = time.time();
t = time.time();
while t < t0 + duration:
   for i in range(1,speed):
      field = dynamics(field);
   for i in range(1,M-1):
     data[:,i] = data[:,i-1];
   data[:,0] = field;


   if omega != 0:
      h = sin(omega*2*pi*t);
      s = sin(omega*sqrt(2.0)*pi*t);
      rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1);
      CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2]);
   teh_displayi(real(data+1)/2,CM);
   t = time.time();
#    for i in range(1,N-1):
#       data[i,:] = data[i-1,:];
#    data[0,:] = field;



