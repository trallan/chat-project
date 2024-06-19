import socket

HOST = 'localhost'
PORT = 9040

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

try:
  while True:
    msg = input('Enter message: ')
    if msg.lower() == 'exit':
      break  # Exit the loop and close the connection if 'exit' is entered
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print('Received from server:', data.decode('utf-8'))
except KeyboardInterrupt:
  print('Client shutting down...')
except Exception as e:
  print('Exception occurred:', e)
finally:
  s.close()
  print('Client closed')
