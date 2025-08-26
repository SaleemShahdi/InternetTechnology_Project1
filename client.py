import threading
import time
import random
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
    
# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

# Receive data from the server
data_from_server=cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

message = input("Input a message: ")
print("Here is what you sent in: " + message)
cs.send(message.encode("utf-8"))
message = cs.recv(1024).decode("utf-8")
print("Here is what you received from the server: " + message)
message = ""


with open("in-proj.txt", "r") as infile:
    for line in infile:
        message = message + line
        # message = line.strip()
        # cs.send(message.encode("utf-8"))


# close the client socket
cs.send(message.encode("utf-8"))
cs.close()
exit()