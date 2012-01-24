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

if len(sys.argv) < 7:
   CM = colormap.MATLAB_COLORMAP;
   omega = 0;
elif len(sys.argv) == 7:
   omega = float(sys.argv[6]);
elif len(sys.argv) == 9:
   omega = 0;
   CM = colormap.solid_colormap(float(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]));


N = 50;
M = 24;
data =1*random.randn(N,M);

X = zeros([N,M]);
Y = zeros([N,M]);

for i in range(0,N):
   X[i,:] = (i-(N/2.0))/(M/2.0);
for i in range(0,M):
   Y[:,i] = (i-(M/2.0))/(M/2.0);

X = reshape(X,[1,N*M]);
Y = reshape(Y,[1,N*M]);
G = concatenate((X,Y));

t=0;
theta = 0;
def dynamics(data,verbose=0):
   global theta;
   dt = 0.1;
   theta = theta + dt;
   R = matrix([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
   I = R*G;
   V = matrix([1,-1])*(array(I)*array(I));
   data = reshape(V,[N,M]);
   return data;
t=0;

import colorsys;
import time;
h = 0;
s = 0;



t0 = time.time();
t = time.time();
from time import sleep as wakeup;

CM = 1-colormap.MATLAB_COLORMAP;

while t < t0 + duration:
   teh_displayi((1+data/5)/2,CM);
   data = dynamics(data);
   wakeup(0.005)
   t = time.time();
