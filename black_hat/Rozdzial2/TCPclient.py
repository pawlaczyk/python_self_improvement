#coding=utf-8

import socket

target_host="www.wp.pl"
target_port=80

#utworzenie obiektu gniazd TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#polączenie się z klientem
client.connect((target_host, target_port))

#wysyłanie danych
client.send(" ")

#odebranie danych
response = client.recv(4096)

print response