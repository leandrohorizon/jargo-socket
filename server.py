import socket
import requests
import json
import random

def speak(text):
  request = requests.get(f"http://localhost:3000/api/v1/robots/1/speak?text={text}")
  todo = json.loads(request.content)
  responses = todo['interaction']['responses']
  quantity_responses = len(responses)
  if(quantity_responses > 0):
    response_sort = responses[random.randint(0, quantity_responses-1)]['response']
    print(f"Jargo: {response_sort['text']}")
    exec(response_sort['command'])
  else:
    print('Sem resposta')

def exec(command):
  print(command)

def start():
  HOST = ''              # Endereco IP do Servidor
  PORT = 5000            # Porta que o Servidor esta
  udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  orig = (HOST, PORT)
  udp.bind(orig)
  while True:
    msg, cliente = udp.recvfrom(1024)
    speak(msg)

start()