import socket
import threading
from chat import Chat

PORT = 7447

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = socket.gethostbyname(socket.gethostname())
    HOST_INFORMATION = (address, PORT)
    s.bind(HOST_INFORMATION)

    print("[SERVER STARTS] server is starting...")
    s.listen()
    client_handler(s)

def client_handler(server):
    chat = Chat()

    conn, address = server.accept()
    print('[NEW CONNECTION] connected from {}'.format(address))

    sender = threading.Thread(target=chat.send_handler, args=(conn, ))
    sender.start()

    receiver = threading.Thread(target=chat.recv_msg, args=(conn, ))
    receiver.start()

    sender.join()
    receiver.join()
    print('[CLOSE CONNECTION] {}'.format(address))
    conn.close()

if __name__ == '__main__':
    main()