import socket
import requests
import json

previous_reaction_id = None

def speak(keywords):
  global previous_reaction_id

  request = requests.get('https://jargorobots.herokuapp.com/api/v1/robots/jargo/speak',
                         data={'keywords': keywords,
                               'previous_reaction_id': previous_reaction_id})

  todo = json.loads(request.content)
  interaction = todo['interaction']

  if(interaction['id'] is None):
    print('Sem resposta')
    return

  previous_reaction_id = interaction['id']
  reaction = interaction['reaction']
  print(f"Jargo: {reaction['text']}")
  exec(reaction['command'])


def exec(command):
  print(f"command: {command}")

def start():
  print('iniciado')
  HOST = ''
  PORT = 5000
  udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  orig = (HOST, PORT)
  udp.bind(orig)
  while True:
    msg, cliente = udp.recvfrom(1024)
    speak(msg)

start()
