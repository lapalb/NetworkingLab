import socket
import sys
import argparse
host = 'localhost'
data_payload = 2048
backlog = 5 
cl=dict()
def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    client, address = sock.accept() 
    while True: 
        
        data = client.recv(data_payload).decode('ascii')
        print("the data:", data)
        if(data=='r'):
            Username=client.recv(256).decode('ascii')
            if Username not in cl:
                cl[Username]=0;
                mess="You are registered".encode('ascii')
                client.send(mess)
            else:
                mess="There is already a user with this name".encode('ascii')
                client.send(mess)



        if(data=='v'):
            mess=str(cl.keys()).encode('ascii')
            client.send(mess)
            voter=client.recv(256).decode('ascii')
            cl[voter]=cl[voter]+1;

            mess="You voted for Candidate " + str(voter)
            mess=mess.encode('ascii')
            client.send(mess)


        if(data=='e'):
            mess=str(cl.items()).encode('ascii')
            client.send(mess);


   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    echo_server(port)
