#!/usr/bin/python3
# v4quero 08/03/2020
# Port Scanner V0.1

# here we will call our socket library. giving us access to network resources
import socket
import subprocess
import sys
from time import sleep
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
port_inp1 = int(input("Enter your starting port: "))
port_inp2 = int(input("Enter your ending port: "))
# Print information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()
# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors


try:

    for port in range(port_inp1,port_inp2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))

        sock.close()


except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t3 = datetime.now()
total = t3 - t1

# Calculates the difference of time, to see how long it took to run the script
print("Total scan time: ", str(total))
# Printing the information to screen


