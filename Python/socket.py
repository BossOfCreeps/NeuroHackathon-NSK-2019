import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 8005))

data = sock.recv(1024)
sock.close()

print ((data[0])-48)
