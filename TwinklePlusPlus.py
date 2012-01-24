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
   omega1 = -1;
elif len(sys.argv) == 5:
   omega1 = float(sys.argv[4]);
   omega2 = sqrt(2.0)*float(sys.argv[4]);
elif len(sys.argv) == 6:
   omega1 = float(sys.argv[4]);
   omega2 = float(sys.argv[5]);
elif len(sys.argv) == 7:
   omega1 = -1;
   CM = colormap.solid_colormap(float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]));

N = 50;
M = 24;
data = 0.01*random.randn(N,M);

dt = speed*0.005;

d0 = zeros([N,M]);
def dynamics(data,verbose=0):
   global d0;
   global dt;
   dA = d0 - data;
   data = data + dt*dA
   return data;


from scipy.stats import poisson;
from time import sleep as wakeup
import time;
h = 0;
s = 0;

t0 = time.time();
t = time.time();

n=0;
while t < t0 + duration:
   from time import sleep as wakeup
   n=n+1;

   if omega1 != -1:
      h = cos(omega1*2*pi*t);
      s = sin(omega2*pi*t+pi/2);
      rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1);
      CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2]);
   teh_displayi(sin(data),CM);
   t = time.time();

   c = poisson.rvs(mu,size=1);
   for i in range(0,c):
      x = floor(N*random.rand());
      y = floor(M*random.rand());
      d0[x][y] = d0[x][y] + 3.14159265;

   data = dynamics(data);
   wakeup(0.005)
