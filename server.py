import socket
import threading
import logging

logging.basicConfig(filename='server.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s')

HOST = 'localhost'
PORT = 9040


def handle_client(conn, addr):
  print('Connected by', addr)
  logging.info(f'Connected by {addr}')
  try:
    while True:
      data = conn.recv(1024).decode('utf-8')
      if not data:
        break  # Exit the loop if no data is received (client has closed the connection)
      logging.info(f'Received from {addr}: {repr(data)}')
      print('Received from', addr, ':', repr(data))
      # Send acknowledgment back to the client
      conn.send(f"Server received: {data}".encode('utf-8'))
  except Exception as e:
    print('Exception occurred while handling connection:', e)
    logging.error(f'Exception occurred while handling connection: {e}')
  finally:
    conn.close()
    print('Connection closed', addr)
    logging.info(f'Connection closed {addr}')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Server is listening...')

try:
  while True:
    conn, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
except KeyboardInterrupt:
  print('Server shutting down...')
  logging.info(f'Server shutting down...')
except Exception as e:
  print('Exception occurred:', e)
  logging.info(f'Exception occurred: {e}')
finally:
  s.close()
  print('Server closed')
  logging.info('Server closed')
