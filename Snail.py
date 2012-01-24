#!/usr/bin/env python

import sys;
from numpy import *;
from scipy.signal import correlate2d;
from teh_display import *;

if len(sys.argv) < 2:
   duration = 10;
else:
   duration = float(sys.argv[1])

N = 50;
M = 24;

screen = zeros([N,M]);

dt = 0.5;
t=0;

import colorsys;
import time;


t0 = time.time();
t = time.time();
from time import sleep as wakeup;

# First bounce simulation:
x = array([10,10]);
v = array([1,0.2]);
sz = array([4*N,M]);
CM = colormap.BLUE_COLORMAP;
while t < t0 + duration:
   x = x + dt*v;
   coll = 0;
   for k in range(0,10):
      for i in range(0,2):
         if x[i] > sz[i]-1:
            x[i] = 0;
            #v[i] = -abs(v[i]);
            if i == 0:
               coll = 1;
         elif x[i] < 0:
            x[i] = sz[i]-1;
            #v[i] = abs(v[i]);
            coll = 1;
      if coll:
         h = random.rand();
         s = random.rand();
         rgb = colorsys.hsv_to_rgb(h,1,1);
         CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2]);
      screen = 0.995*screen;
      if x[0] < N-1:
         screen[x[0],x[1]] = 1;#screen[x[0],x[1]]+0.3;
   teh_displayi(screen,CM);
   t = time.time();
#   wakeup(0.005)
