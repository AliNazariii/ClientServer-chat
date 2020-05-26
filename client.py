import socket

PORT = 7447

MESSAGE_LENGTH_SIZE = 64

ENCODING = 'utf-8'

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = socket.gethostbyname(socket.gethostname())
    SERVER_INFORMATION = (address, PORT)
    s.connect(SERVER_INFORMATION)

    while True:
        input_string = input()
        send_msg(s, input_string)
        if input_string == 'DISCONNECT': break

def send_msg(client, msg):
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(msg_length))

    client.send(msg_length)
    client.send(message)

if __name__ == '__main__':
    main()