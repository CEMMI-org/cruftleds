import display
from numpy import zeros
data=zeros([150])
data[0:3]=255
#print data
sockets=display.make_sockets(["36"])
display.display(data,sockets[0])

