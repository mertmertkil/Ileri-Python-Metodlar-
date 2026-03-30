import socket

POST = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,POST)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNETC_MESSAGE = "quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

while True:
    message = client.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNETC_MESSAGE:
        client.send("Çıkış yapıldı.".encode(FORMAT))
        break
    else:
        print(f"{message}")
        message = input("mesaj: ...")
        client.send(message.encode(FORMAT))

client.close()