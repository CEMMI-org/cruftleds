#!/usr/bin/env python


# Arguments:
#
# Duration -- time to run in secs.
# Speed -- Fade rate for lights (they fade in then immediately out), 1-10 reas.
# Arrival Rate -- How quickly to add lights (1 is reasonable).
# 
#
# Then either:
#
# nothing: use WHITE colormap.
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
   speed = 1;
else:
   speed = int(sys.argv[2]);

if len(sys.argv) < 4:
   mu = 1;
else:
   mu = float(sys.argv[3]);

if len(sys.argv) < 5:
   CM = colormap.solid_colormap(1,1,1);
   omega = 0;
elif len(sys.argv) == 5:
   omega = float(sys.argv[4]);
elif len(sys.argv) == 7:
   omega = 0;
   CM = colormap.solid_colormap(float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]));

N = 50;
M = 24;
data = zeros([N,M]);
dataQ = zeros([N,M]);

X = zeros([N,M]);
Y = zeros([N,M]);

for i in range(0,N):
   X[i,:] = (i-(N/2.0))/(M/2.0);
for i in range(0,M):
   Y[:,i] = (i-(M/2.0))/(M/2.0);

X = reshape(X,[1,N*M]);
Y = reshape(Y,[1,N*M]);
G = concatenate((X,Y));


dt = 0.005;

d0 = zeros([N,M]);
def dynamics(data,verbose=0):
   global d0;
   global dt;
   dA = d0 - data;
   data = data + speed*dt*dA
   return data;

def dynamicsQ(theta):
   global dt
   R = matrix([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
   I = R*G;
   V = matrix([1,-1])*(array(I)*array(I));
   data = reshape(V,[N,M]);
   return data;
 

from scipy.stats import poisson;
from time import sleep as wakeup
import time;
h = 0;
s = 0;

t0 = time.time();
t = time.time();
theta = 0
n=0;
while t < t0 + duration:
   from time import sleep as wakeup
   n=n+1;

   if omega != 0:
      h = sin(omega*2*pi*t);
      s = sin(omega*sqrt(2.0)*pi*t);
      rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1);
      CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2]);
   
   tw = zeros([3*N,M]);
   for j in range(0,M):
      tw[:,j] = colormap.i2c(sin(data[:,j]),colormap.WHITE_COLORMAP);
   Q = zeros([3*N,M]);
   for j in range(0,M):
      Q[:,j] = colormap.i2c(dataQ[:,j],colormap.MATLAB_COLORMAP);
  
   teh_display(tw*Q);
   t = time.time();

   c = poisson.rvs(mu,size=1);
   for i in range(0,c):
      x = floor(N*random.rand());
      y = floor(M*random.rand());
      d0[x][y] = d0[x][y] + 3.14159265;

   theta = theta + 8*dt;

   dataQ = dynamicsQ(theta);
   data = dynamics(data);
   wakeup(0.005)
