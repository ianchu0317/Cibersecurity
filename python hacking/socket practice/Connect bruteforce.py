import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
port = input("[+] Insert port to listening: ")
ADDR = (SERVER, int(port))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_connection(conn, addr):
    print (f"Client {addr} has been connected succefully")
    connected = True

    while connected:
        length = conn.rcv(64).decode("utf-8")
        length = len(length)
        msg = conn.rcv(length).decode("etf-8")
        print (f"{addr}: {msg}")

        if msg == "disconnect":
            connected = False
            print("Disconnected succefully :)")
    conn.close()


def listening(server):
    server.listen()
    try:
        conn, addr = server.accept()
        print("")
        connection =threading.Thread(target="handle_connection", args="conn, addr")
        connection.start()
        print (f"[ACTIVE SESSIONS]: {threading.active_Count -1}")

    except KeyboardInterrupt:
        print("The connection has been interrupted :)")
    except:
        print("An error has ocurred")


try:
    print (f"[LISTENING] {SERVER}:{port}: ")
    listening(server)
except KeyboardInterrupt:
    print ("The connection has been interrupted :)")