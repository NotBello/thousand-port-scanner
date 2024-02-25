
#!/usr/bin/python

# Using Python 3
# Created Venujan Malaiyandi 
# Second Iteration of a simple port scanner
# Converting the existing codebase for single port scanner into thousand port scanner
# To check for a thousand ports
# Using socket library 


# importing libraries 
import socket
from termcolor import colored

# Create socket objects with IPv4 and TCP protocol
socketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Defualt Time as 1 second
socket.setdefaulttimeout(1)

# Declaring host and port details
host = input("[*] Enter The Host To Scan: ")

# Defining portscanner function
def scanPort(port):
	if socketA.connect_ex((host, port)):
		print(colored("[!] Port %d is closed" % (port), 'red'))
	else:
		print(colored("[+] Port %d is open" % (port), 'green'))

for port in range(1,1001):
	scanPort(port)
