import threading
import time
import random
import socket

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.  
msg = "Welcome to CS 352!"
csockid.send(msg.encode('utf-8'))
message = csockid.recv(1024).decode("utf-8")
message = message[::-1].swapcase()
csockid.send(message.encode("utf-8"))

with open("out-proj.txt", "w") as outfile:
    message = csockid.recv(1024).decode("utf-8")
    messageList = message.split("\n")
    length = len(messageList)
    for i in range(0,length):
        messageList[i] = messageList[i][::-1].swapcase()
    for i in range(0, length-1):
        outfile.write(messageList[i]+"\n")
    outfile.write(messageList[length-1])
    # outfile.write(message)
    #csockid, addr = ss.accept()
    



    


# Close the server socket
ss.close()
exit()