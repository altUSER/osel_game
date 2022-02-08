#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9091))

sock.send('hello, world!')
data = sock.recv(1024)
print(data)
sock.close()
