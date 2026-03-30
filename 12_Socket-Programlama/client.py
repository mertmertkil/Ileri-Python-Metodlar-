import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# ilk parametre IP4 şeklinde bir ıp adresi, ikinci parametre de TCP protokolünü temsil eder.

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345 # rastgele bir port yazdım.
client_socket.connect((HOST, PORT))

message = client_socket.recv(1024) # parametre mesajın max byte.
print(message.decode("utf-8"))
client_socket.close()
