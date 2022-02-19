import socket
HOST = '192.168.1.3'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('client started\n')

msg = 'leanddro conectado..'

while True:
  udp.sendto(msg.encode(), dest)
  msg = input()

