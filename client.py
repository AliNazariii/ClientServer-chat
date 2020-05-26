import socket
import threading
from chat import Chat

PORT = 7447

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = socket.gethostbyname(socket.gethostname())
    SERVER_INFORMATION = (address, PORT)
    s.connect(SERVER_INFORMATION)
    print('[START CONNECTION]')

    client_handler(s)

def client_handler(client):
    chat = Chat()

    sender = threading.Thread(target=chat.send_handler, args=(client, ))
    sender.start()

    receiver = threading.Thread(target=chat.recv_msg, args=(client, ))
    receiver.start()

    sender.join()
    receiver.join()
    print('[CLOSE CONNECTION]')
    client.close()

if __name__ == '__main__':
    main()