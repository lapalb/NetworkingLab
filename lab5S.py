import socket
import argparse
import sys

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=localhost
port=8000
server_address=(host,port)
sock.connect(server_address)
sock.listen(5)

while True:
	print "Waiting to receive message from client"
	client, address = sock.accept()
	data = client.recv(data_payload)
	if data:
		print "Data: %s" %data
		client.send(data)
		print "sent %s bytes back to %s" % (data, address)
	# end connection
	client.close()
