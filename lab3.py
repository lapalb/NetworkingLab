# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:52:34 2019

@author: Ashish Jha
"""

import socket
#print(dir(socket))

#Getting the hostname
print("The Nmae of the host is ",socket.gethostname())
print("The IP of the host is ",socket.gethostbyname(socket.gethostname()))

#IP Address Conversion
addr1 = socket.gethostbyname('google.com')
print("The Ip of Goolge(Remote Machine) is ", addr1)
ipl=addr1.split('.')
print("The Ip of Goolge(Remote Machine) BIN ",end=" ")
for x in ipl:
    print(bin(int(x))[2:],end=" ")
print("\nThe Ip of Goolge(Remote Machine) Hex ",end=" ")
for x in ipl:
    print(hex(int(x))[2:],end=" ")
    
    
#Getting the Service Name
print("\nThe Service Name is ",socket.getservbyport(80,"tcp"))

#Getting Time
import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org',version=3)
print(ctime(response.tx_time))


#Blocking Socket
clientSocket=socket.socket()
host=socket.gethostname()
clientSocket.connect((host,12345))
clientSocket.setblocking(0)