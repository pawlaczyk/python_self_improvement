#coding=utf-8

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Nasuchiwanie na porcie{0}:{1}".format(bind_ip, bind_port)

#wątek do obsługi klienta
def handle_client(client_socket):
	#drukuje informacje przesłane przez klienta
	request = client_socket.recv(1024)
	print "[*] Odebrano: {0}".forma(request)
	#wysyła pakiet z powrotem
	client_socket.send("ACK!")
	client_socket.close()

while True:
	client, addr = server.accept()
	print "[*] Przyjęto połączenie od: {0}:{1}".format(addr[0], addr[1])
	#utworzenie wątku klienta do obsługi przychodzących danych
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()