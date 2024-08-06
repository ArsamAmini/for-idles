import socket
from _thread import *
import sys

server = "localhost"
port = 8888

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    listening_socket.bind((server, port))
except socket.error as e:
    print(str(e))

listening_socket.listen(4)
print("Waiting for a connection")

def threaded_client(conn):
    conn.send(str.encode("Connected, this is my message"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

                conn.sendall(str.encode(reply))
        except Exception as e:
            print(f"this the error : {e}")
            break

        print("Connection lost")
        conn.close()

while True:
    conn, addr = listening_socket.accept()
    print("Connecting to: ", addr)

    start_new_thread(threaded_client, (conn,))