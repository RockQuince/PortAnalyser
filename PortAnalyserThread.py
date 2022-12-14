#Lucas Rocha Faria Costa RM93963
#Atividade portscanner - 1TDCF
#Primeiramente importamos as bibliotecas que serão utilizadas, para garantir que todas as funções funcionem como desejado
import sys
import socket
import threading
from datetime import datetime
#Nessa etapa, definiremos um alvo, porta inicial e porta final, respectivamente, para dessa forma ser possivel definir um range desejado sem muita espera
#Apenas uma intrudução estetica ao programa
print(".----.  .----. .----.  .---.  .--.  .-. .-.  .--.  .-. .-.  .-..---. .----..----.  ")
print("| {}  }/  {}  \| {}  }{_   _}/ {} \ |  `| | / {} \ | |  \ \/ /{_   / | {_  | {}  } ")
print("| .--' \      /| .-. \  | | /  /\  \| |\  |/  /\  \| `--.}  {  /    }| {__ | .-. \ ")
print("`-'     `----' `-' `-'  `-' `-'  `-'`-' `-'`-'  `-'`----'`--'  `---' `----'`-' `-' ")
try:
    #Aqui definiremos o alvo, onde sera definido logo ao inicir o programa
    alvo = input("Digite o IP alvo: ")
    #Aqui definiremos o range inicial e logo em seguida o range final
    rangestart = int(input("Digite o alcance inicial desejado: "))
    rangestop = int(input("Digite o alcance final desejado: "))
    print("--------------------------------------------")
    print("Analizando alvo: " + alvo)
    tinicio = datetime.now()
    print("Analize começou as:" + str(datetime.now()))
    print("--------------------------------------------")
    #Nessa etapa, defini a função "analise" para posteriormente usa-la como alvo de uma thread, a fim de acelerar o processo de scan
    def analise(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        if s.connect_ex((alvo,port)) == 0:
            print("Porta {} esta aberta e o Serviço que esta sendo executado nessa porta é:".format(port)+ socket.getservbyport(port))
        s.close()
    analizadas=1
    #Aqui utilizamos do range que foi definido anteriormente
    for x in range(rangestart, rangestop+1):
        t=threading.Thread(target=analise,kwargs={'port':analizadas})
        analizadas+=1
        t.start()
    tfim = datetime.now()
    scantime=tfim-tinicio
    print("--------------------------------------------")
    print("Analize terminou em:", scantime)
    print("--------------------------------------------")
    #Por fim algumas exceptions
except KeyboardInterrupt:
        print("\n Ctrl+C foi apertado")
        print("\n Cancelando processo e parando execussão do programa")
        sys.exit()
except socket.error:
        print("\n Servidor não esta respondendo")
        print("\n Cancelando processo e parando execussão do programa")
        sys.exit()
except socket.gaierror:
        print("\n Hostname não pode ser definido")
        print("\n Cancelando processo e parando execussão do programa")
        sys.exit()
