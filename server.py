import socket
from _thread import *
import sys
import time

server = "localhost"
port = 8888

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    listening_socket.bind((server, port))
except socket.error as e:
    print(str(e))

listening_socket.listen(4)
print("Waiting for a connection")

TIME_WINDOW = 10
MAX_REQUESTS = 5
request_times = {}

def threaded_client(conn):
    conn.send(str.encode("Connected, this is my message"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # receive data
            if not data:
                print("Disconnected") # disconnect if there is no data
                break
            else:
                current_time = time.time() # get current time for ddos controlling
                if addr[0] not in request_times: # if this is a new ip
                    request_times[addr[0]] = [] # add this ip into request_times and give it a list
                request_times[addr[0]] = [t for t in request_times[addr[0]] if current_time - t < TIME_WINDOW] # if the last request of this ip was more than 10 seconds ago filter it
                if len(request_times[addr[0]]) < MAX_REQUESTS: # if the len of this ip requests were less than 5
                    request_times[addr[0]].append(current_time) # add now to the list
                    reply = data.decode("utf-8") # everything is ok so decode data
                    print("Received: ", reply)
                    print("Sending: ", reply)
                    conn.sendall(str.encode(reply)) # then encode again and send
                    return False
                else:
                    return True
        except Exception as e:
            print(f"this the error : {e}")
            break

    print("Connection lost")
    conn.close()

while True:
    conn, addr = listening_socket.accept()
    print("Connecting to: ", addr)

    start_new_thread(threaded_client, (conn,))
