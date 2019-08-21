#coding=utf-8

import sys
import socket
import threading

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.bind((local_host, local_port))
	except:
		print "[!] Nieudana próba nasłuchu na porcie {0}:{1}".format(local_host,local_port)
		print "[!] Poszukaj innego gniazda lub zdobądź odpowiednie uprawnienia"
		sys.exit(0)
		print "[*] Nasłuchiwanie na porcie {0}:{1}".format(local_host, local_port)

		server.listen(5)

		while True:
			client_socket, addr = server.accept()

			#wydruk informacji o połączeniu lokalnym
			print "[=>] Otrzymano połączenie przychodzące od {0}:{1}".format(addr[0], addr[1])

			#uruchomienie wątku do współpracy ze zdalnym hostem
			proxy_thread = threading.Thread(target=proxy_handler, 
				args=(client_socket, remote_host, remote_port, receive_first) )

			proxy_thread.start()

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
	#połączenie ze zdalnym hostem
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connect((remote_host, remote_port))

	#odebranie danych od zdalnego hosta w razie potrzeby
	if receive_first:
		remote_buffer = receive_from(remote_socket)
		hexdump(remote_buffer)

		#wysyłanie danych i procedury obsługi odpowiedzi
		remote_buffer = response_handler(remote_buffer)

		#jeśli mamy dane do wysyłania do klienta lokalnego, to je wysyłamy
		if len(remote_buffer):
			print "[<=] Wysyłanie {0} bajtów do {1}".format(len(remote_buffer))
			client_socket.send(remote_buffer)

		#uruchamiamy pętle, w której odczytujemy dane z hostla lokalnego
		#wysyłamy dane do hosta zdalnego, wysyłamy dane do hosta lokalnego
		#wszystko powtarzamy
		while True:
			local_buffer = receive_from(client_socket)

			if len(local_buffer):
				print "[=>] Odebrano {0} bajtów od localhost".format(local_buffer)
				hexdump(local_buffer)

				#wysyłanie danych do procedury obsugi żądań
				local_buffer = request_handler(local_buffer)

				#przesyłanie danych do zdlanego hosta
				remote_socket.send(local_buffer)
				print "[=>] Wysyłano do zdalnego hosta"

				#odebranie odpowiedzi
				remote_buffer = receive_from(remote_socket)

				if len(remote_buffer):
					print "[<=] Odebrano {0} bajtów od zdalnego hosta".format(len(remote_buffer))
					hexdump(remote_buffer)

					#wysyłanie danych do procedury obsługi odpowiedzi
					remote_buffer = response_handler(remote_buffer)

					#wysyłanie odpowiedzi do lokalnego gniazda
					client_socket.send(remote_buffer)

					print "[<=] Wysyłano do localhost."

				#jeśli nie ma więcej danych po żadnej ze stron, zamykamy połaczenia
				if not len(local_buffer) or not len(remote_buffer):
					client_socket.close()
					remote_socket.close()
					print "[*] Nie ma więcej danych. Zamykanie połączeń"
					break


		def main():
			#żadnego dziwnego przetwarzania wiersza poleceń
			if len(sys.argv[1:]) != 5:
				print """Sposób użycia: ./proxy.py [localhost] [localport] [remotehost [remoteport] [receive_first] 
				przykład: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"""
				sys.exit(0)

			#konfiguracja lokalnych parametrów nasłuchu
			local_host = sys.argv[1]
			local_port = sys.argv[2]

			#ustawienie zdalengo celu
			remote_host = sys.argv[3]
			remote_port	= int(sys.argv[4])

			#nakazujemy proxy nawiązanie połączenia i odebrania danych
			#przed wysłaniem danych do zdalengo hosta
			receive_first = sys.argv[5]

			if "True" in receive_first:
				receive_first = True
			else:
				receive_first = False

			#włączamy gniazdo do nasłuchu
			server_loop(local_host, local_port, local_port, remote_host, remote_port, receive_first)
		main()

#Jest to elegancka funkcja do robienia zrzutów szesnastkowych wydobyta wprost z komentarzy
#na stronie: http://code.activestate.com/recipes/142812-hex-dumper/
def hexdump(src, length=16):
	result = []
	digits = 4 if isinstance(src, unicode) else 2
	for i in xrange(0, len(src), length):
		s = src[i:i+length]
		hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
		text = b''.join([x if 0x20 <= ord(x) <0x7F else b'.' for x in s])
		result.append( b"%04X %-*s %s" % (i, length*(digits + 1), hexa, text))

	print b'\n'.join(result)

def receive_from(connection):
	buffer = ""

	#ustawiamy 2 sekundowy limit czasu; w niektórch przypadkach może być konieczna
	# zmiana tej wartosci
	connection.settimeout(2)

	try:
		#wczytujemy dane do bufora, aż wczytamy wszystkie
		#albo skończy nam się czas
		while True:
			data = connection.recv(4096)

			if not data:
				break
			buffer += data
	except:
		pass

	return buffer


#Modyfikujemy żądania przeznaczone dla zdalnego hosta
def request_handler(buffer):
	#Modyfikujemy pakiety
	return buffer

#Modyfikujemy odpowiedzi przeznaczone dla lokalnego hosta
def response_handler(buffer):
	#Modyfikujemy pakiety
	return buffer

#do testow
#sudo ./TCPproxy.py 127.0.0.1 21 ftp.target.ca 21 True 
#sudo bo port 21 jest uprzywilejowany + ustawić swojego proxy na serwert ftp który będzie odpowiadał