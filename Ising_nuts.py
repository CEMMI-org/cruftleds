#!/usr/bin/env python

import sys;
from numpy import *;
from scipy.signal import correlate2d;
from teh_display import *;

N = 50;
M = 24;
data = 0.01*random.randn(N,M);

dt = 0.005;
t=0;
alpha = -2;
beta  = 0.00001;

def dynamics(data,verbose=0):
   global beta;
   dA = correlate2d(data,array([[1,1,1],[1,0,1],[1,1,1]]),boundary='wrap');
   dA = dA[1:N+1,1:M+1];

   r = random.rand(N,M);

   data = 2*floor(r*(1+exp(beta*dA)))-1;
   return data;
t=0;

def unnecessary():
   from time import sleep as wakeup
   global dt;
   global data;
   global alpha;
   global beta;
   global t;
   t=t+1;
   teh_displayi(real(data+1)/2);
   #imdisplayi(real(data+1)/2,sockets,mapping)
   #imdisplayi(abs(data),sockets)
   for i in range(0,10):
     data = dynamics(data);
   #data[23,0] = 0;
   wakeup(0.005)
   #for s in sockets:
   #   displayi(transpose(real([(data+1)/2])),s)
   #   displayi(transpose(real([(data+1)/2])),s,2)

import colorsys;
import time;
h = 0;
s = 0;



t0 = time.time();
t = time.time();
from time import sleep as wakeup;

if len(sys.argv) < 2:
   duration = 10;
else:
   duration = float(sys.argv[1])

while t < t0 + duration:
   unnecessary();
   t = time.time();
