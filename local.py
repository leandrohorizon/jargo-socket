import requests
import json
import os
import speech_recognition as sr

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

  reaction = interaction['reaction']
  previous_reaction_id = reaction['id']
  print(f"Jargo: {reaction['text']}")
  exec(reaction['procedures'])


def exec(procedures):
  for procedure in procedures:
    procedure = procedure['procedure']
    command = procedure['command']

    for (dirpath, dirnames, filenames) in os.walk("./mods/"):
        for filename in filenames:
            if filename.replace('.py', '') == command:
                print(f"executando: {filename}")
                os.system(f"python mods/{filename}")
                return

#Função para ouvir e reconhecer a fala
def listen():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    speak(frase)

listen()