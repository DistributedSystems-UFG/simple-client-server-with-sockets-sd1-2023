from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
s.send(str.encode('Hello, world'))  # send some data
data = s.recv(1024)     # receive the response
print (pickle.load(data))            # print the result
s.close()               # close the connection
