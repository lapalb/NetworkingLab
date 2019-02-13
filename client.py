import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print ("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    try:
        while(1):
            message = str(input("Enter r to register, e for exit and v for vote"))
            print ("Sending %s" % message)
            sock.sendall(message.encode('ascii'))
            if(message=='r'):
                Username=str(input("Enter Candidate Name"))
                sock.send(Username.encode('ascii'))
                data = sock.recv(256)
                print ("Received: %s" % data)
            if(message=='e'):
                data = sock.recv(256)
                print ("Received: %s" % data)
            if(message=='v'):
                data = sock.recv(256)
                print ("Candiate list : %s" % data);
                candidate=str(input("Enter Usename of Candiate"))
                sock.send(candidate.encode('ascii'))
                data=sock.recv(256)
                print (data);
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    echo_client(port)
