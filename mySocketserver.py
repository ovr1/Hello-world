import socket


def Main():
    ip = '192.168.0.19'
    port = 5001

    mySocket = socket.socket()
    mySocket.bind((ip, port))

    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))

        data = str(data).upper()
        print("Received from User: " + str(data))

        data = input(" ? ")
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()