import socket
import threading
import PySimpleGUI as sg

client = socket.socket()
client.connect(('127.0.0.1', 4444))

window_title = "Messager"
layout = [
    [sg.Multiline(size=(80, 40), key="-OUTPUT-", disabled=True, autoscroll=True)],
    [sg.Text("Nome:"), sg.InputText(key="-NAME-"), sg.Button("Set Name")],
    [sg.Text("Mensagem:"), sg.InputText(key="-MSG-"), sg.Button("Enviar"), sg.Button("Sair")]
]

window = sg.Window(window_title, layout,size=(1000,1000))

nome = None

def handle_mensagens():
    while True:
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        received_message = mensagem_splitada[1] + ": " + mensagem_splitada[2]
        window["-OUTPUT-"].update(received_message + "\n", append=True)


def enviar(mensagem):
    client.send(mensagem.encode('utf-8'))


def iniciar():
    thread = threading.Thread(target=handle_mensagens)
    thread.start()
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        if event == "Set Name":
            nome = values["-NAME-"]
            enviar("nome=" + nome)
        if event == "Enviar":
            mensagem = values["-MSG-"]
            enviar("msg=" + mensagem)

    window.close()
    client.close()

iniciar()
