# broadcast query irobot Roomba from LAN
from socket import *  
import socket

UDP_IP = "255.255.255.255"  # broadcast (if you know your irobot lan ip, you can change to that one)
UDP_PORT = 5678
MESSAGE = "irobotmcs"

s0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s0.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s0.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s0.bind(("", UDP_PORT))
print "Looking for robots...\r\n"

s0.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while 1:
    rev = s0.recvfrom(1024)
    revdata = rev[0]
    revaddr = rev[1]
    print revdata, "[from]", revaddr

s0.close()

