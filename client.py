import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4444))


def handle_mensagens():
    while (True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])


def enviar(mensagem):
    client.send(mensagem.encode('utf-8'))


def enviar_mensagem():
    mensagem = input("")
    enviar("msg=" + mensagem)


def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)


def iniciar_envio():
    enviar_nome()
    while True:
        enviar_mensagem()


def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()


iniciar()
