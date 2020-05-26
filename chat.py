class Chat:
    def __init__(self):
        self.running = True
        self.MESSAGE_LENGTH_SIZE = 64
        self.ENCODING = 'utf-8'
    
    def send_handler(self, conn):
        while self.running:
            input_string = input()
            self.send_msg(conn, input_string)
            if input_string == 'DISCONNECT': 
                print('Wait...')
                self.send_msg(conn, 'Press Enter to exit')
                break
        self.running = False

    def send_msg(self, conn, msg):
        message = msg.encode(self.ENCODING)

        msg_length = len(message)
        msg_length = str(msg_length).encode(self.ENCODING)
        msg_length += b' ' * (self.MESSAGE_LENGTH_SIZE - len(msg_length))

        conn.send(msg_length)
        conn.send(message)

    def recv_msg(self, conn):
        while self.running:
            message_length = int(conn.recv(self.MESSAGE_LENGTH_SIZE).decode(self.ENCODING))
            
            msg = conn.recv(message_length).decode(self.ENCODING)

            if msg == 'DISCONNECT': 
                print('Press Enter to exit')
                break
            
            print('[MESSAGE RECIEVED] {}'.format(msg))
        self.running = False
