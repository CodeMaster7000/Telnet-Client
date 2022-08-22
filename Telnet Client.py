import sys
import telnetlib
HOST = input("Enter Host ID: ")
PORT = input("Enter Port ID: ")
telnet_obj = telnetlib.Telnet(HOST, PORT)
message = ("GET /index.html HTTP/1.1\nHost: "+ HOST +"\n\n").encode('ascii')
telnet_obj.write(message)
output = telnet_obj.read_all()
print(output)
telnet_obj.close()
