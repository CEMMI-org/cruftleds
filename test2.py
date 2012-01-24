import display
from numpy import zeros
from time import sleep
data=zeros([150])
data[0:3]=255
#print data
sockets=display.make_sockets(["36"])
while 1:
  print "do what with data?"
  r=input('>')
  data[0:3]=r
#  import pdb; pdb.set_trace() 
  display.display(data,sockets[0])
  sleep(.001)
