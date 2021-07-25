import socket
HOST = '192.168.1.8'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Conectado\n')
msg = 'leanddro conectado..'

while True:
  udp.sendto (msg, dest)
  msg = raw_input()

