# echo-server.py
import socket

HOST = "127.0.0.1"
PORT = 15555


def parser(data):

    code = data[:4]

    if code == "999":
        pass


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    #to_send = parser(data)
                    conn.sendall(data)
                    print(f"Recieved {data}")


if __name__ == "__main__":
    main()
