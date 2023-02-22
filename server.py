import socket
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000

def setup():
    print("\n\t\t\t\t\t*** Welcome To Tambola Game ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(10)
    print("\t\t\t\SERVER IS WAITING FOR INCOMING CONNECTION... \n")
    
