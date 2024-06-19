import socket

HOST = 'localhost'
PORT = 9040

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

