#coding=utf-8

import socket

target_host="127.0.0.1"
target_port=8080

#utworzenie obiektu gniazda
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_STREAM - TCP; SOCK_DGRAM - UDP

#wysyłanie danych 
client.sendto("Kocham PSIZI",(target_host, target_port)) #send - TCP; sendto - UDP

#odebranie danych
data, addr = client.recvfrom(4096) #recv - TCP; recfrom -UDP

print data
print addr