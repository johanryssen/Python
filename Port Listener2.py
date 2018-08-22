#!/usr/bin/env python2.7
# vim: set ft=py

'''    Simple socket server using threads
'''
import socket
import sys
HOST = ''   # Symbolic name, meaning all available interfaces
#PORT = 1234 # Arbitrary non-privileged port
PORT = input("Enter port number: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
#Start listening on socket
s.listen(10)
print 'Socket now listening on port:', PORT
print 'Remember to allow port', PORT, 'on your firewall'
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
s.close()
