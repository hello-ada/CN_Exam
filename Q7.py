/*Client*/

import os
import sys
path = "/home/saransh/Desktop/port10.txt"
path2= "/home/saransh/Desktop/port11.txt"
fifo = open(path, "w")
fifo.write("fifo based ipc!")
fifo.close()
os.mkfifo(path2)
fifo2=open(path2,"r")
for l in fifo2:
    print l
fifo2.close()

/*Server*/

import os
import sys
path = "/home/saransh/Desktop/port10.txt"
path2 = "/home/saransh/Desktop/port11.txt"
#li=[]
os.mkfifo(path)
fifo = open(path, "r")
for line in fifo:
    print "Received: " + line,
    #li.append(line)
fifo.close()
print()
print("sending data to client....")
fifo2=open(path2,"w")
fifo2.write("fifo based ipc!")
fifo2.close()
