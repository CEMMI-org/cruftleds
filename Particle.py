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
from scipy.signal import correlate2d;

import colormap;
from teh_display import *;
from numpy import *;

duration = 10;

N = 50;
M = 24;
dim = [50,24];

K = 2;
v = zeros([2,K]);
x = zeros([2,K]);
x[0,:] = floor(random.rand(K)*N);
x[1,:] = floor(random.rand(K)*M);
b = 0.9;
def dynamics(verbose=0):
    global b;
    global x;
    global v;
    g = 0.1;
    dt = 0.5;
    data = zeros([N,M]);
    for i in range(0,K):
        v[0,i] = v[0,i] + dt*g;
        for d in range(0,2):
            x[d,i] = x[d,i] + v[d,i]*dt;
            if x[d,i] >= dim[d]:
                x[d,i] = dim[d]-1;
                if d == 1:
                    v[d,i] = -abs(v[d,i])*b;
                else:
                    th = 0.15*(2*random.rand()-1);
                    vp = array([cos(th)*v[0,i]-sin(th)*v[1,i],sin(th)*v[0,i]+cos(th)*v[1,i]]);
                    vp = b*vp;
                    vp[0] = -abs(vp[0]);
                    v[:,i] =array([cos(th)*vp[0]+sin(th)*vp[1],-sin(th)*vp[0]+cos(th)*vp[1]]); 
            elif x[d,i] < 0:
                x[d,i] = 0;
                v[d,i] = abs(v[d,i])*b;
        data[floor(x[0,i]),floor(x[1,i])] = 1;
    return data;


from time import sleep as wakeup
import time;
h = 0;
s = 0;

t0 = time.time();
t = time.time();

Ker = [[0.0064,    0.0318,    0.0730,    0.0730,    0.0318,    0.0064],
    [0.0318,    0.1583,    0.3629,    0.3629,    0.1583,    0.0318],
    [0.0730,    0.3629,    0.8320,    0.8320,    0.3629,    0.0730],
    [0.0730,    0.3629,    0.8320,    0.8320,    0.3629,    0.0730],
    [0.0318,    0.1583,    0.3629,    0.3629,    0.1583,    0.0318],
    [0.0064,    0.0318,    0.0730,    0.0730,    0.0318,    0.0064]];

n=0;
while t < t0 + duration:
   from time import sleep as wakeup
   n=n+1;
   for i in range(0,1):
       data = dynamics();
   dA = correlate2d(data,array(Ker),boundary='fill');
   data = dA[3:N+3,3:M+3];

   teh_displayi(flipud(data),colormap.BLUE_COLORMAP);
   wakeup(0.005)
