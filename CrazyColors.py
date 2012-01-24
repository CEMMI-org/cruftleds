#!/usr/bin/env python

#Use:
#python CrazyColor.py [duration]
#setting duration as 'Inf' [no quotes] has the pattern last indefinitely

import sys;
import scipy;
from time import sleep;
from numpy import *;
from scipy.signal import correlate2d;
from teh_display import *;

N = 50;
M = 24;

#define data - 150 x 4 wide x 3 color values
data = zeros([3*N,M]);

a = scipy.linspace(0,2*scipy.pi,3*N);
q1 = scipy.sin(a)
q2 = scipy.sin(a + scipy.pi/3)
q3 = scipy.sin(a + 2*scipy.pi/3)

rgb = []

for i in range(0,3*N):
  rgb.append([q2[i],q1[i],q3[i]])

for i in range(0,N):
  for j in range(0,M):
    for k in range(0,3):
      data[3*i+k,j] = rgb[i][k];

K = shape(data);
K = K[0]

#####
duration = float(sys.argv[1]);

import time;

t0 = time.time();
t = time.time();
while t < t0 + duration:
  print data[0]
  teh_display(data);
  time.sleep(0.1);
  sv = data[0,:];
  for j in range(0,K-1):
    data[j,:] = data[j+1,:];
    data[K-1,:] = sv;
    t = time.time();

if len(sys.argv) == 5:
  sleep(float(sys.argv[1]))
