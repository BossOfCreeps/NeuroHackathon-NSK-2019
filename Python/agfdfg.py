import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8006
s.send("777".encode()) 
s.close()
