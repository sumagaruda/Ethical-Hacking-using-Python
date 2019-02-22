import socket, sys

target = sys.argv[1]

ports = range(1,2001) #scanning for ports 1-2000

for port in ports:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if sock.connect_ex((target, port)) == 0:

			print "[+] The port {0} is open". format(port)
		#else:
		#	print "[+] The port {0} is closed".format(port)

	except socket.error:
		print "[!] Error with socket"
