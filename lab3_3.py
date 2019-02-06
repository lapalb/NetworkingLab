import socket 
import errno


socket.setdefaulttimeout(10)
print(socket.getdefaulttimeout())

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print ("Strange error creating socket: %s" %e)
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    print ("Couldn't find your port: %s" %e)
    sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print ("Address-related error connecting to server: %s" %e)
    sys.exit(1)
except socket.error as  e:
    print ("Connection error: %s" %e)
    sys.exit(1)

