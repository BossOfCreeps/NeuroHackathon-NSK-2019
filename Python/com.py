import socket
import sys
import serial, time
arduino = serial.Serial('COM12', 9600, timeout=.1)
time.sleep(1) #give the connection a second to settle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8007

s.connect((host, port))
current1 = 0
mean1 = 0
current2 = 0
mean2 = 0
taimer = 2000 # if speed = 1000 per second (2 sec)

i = 0

while True:
        
    i=1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8007
    s.connect((host, port))
    data = arduino.readline()
    
    data1 = data.decode('UTF-8')[0:3]
    data2 = data.decode('UTF-8')[4:7]
    
    
    s.send((data1+data2).encode()) 
s.close()
		
