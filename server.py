import socket

# make a socket server socket = s

s = socket.socket()  # by default it is tcp and ipv4 you we need to change then we have to mention in the braces for ipv6 nad udp
print("Socket Created")

# bind the socket to the IP where we want the server and also assign a port number for now as both the server and the client will be same machine so local host and port any available and allowed
s.bind(('0.0.0.0',9999))

# make a lister so that server is waiting for the clients we can make any number after that the client will be rejected e.g listen(3) waiting for 3 clients 4th will be rejected

s.listen(3)
print("Waiting for Clients")

while True:
    c, addr = s.accept()  # accept clients requests with this it accepts two things the client socket and the address of the client
    
    name = c.recv(1024).decode()
    print(f'Client: {addr} | Name: {name} => Connected')
    
    # send a hello to the client and greet him.
    c.send(bytes('Welcome to the Server','utf-8'))
    
    c.close()


