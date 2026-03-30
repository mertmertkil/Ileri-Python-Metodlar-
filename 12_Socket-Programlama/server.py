import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# ilk parametre IP4 şeklinde bir ıp adresi, ikinci parametre de TCP protokolünü temsil eder.

# HOST = "127.0.0.1" # localhost'u temsil eder. 
# dinamik olarak alalım ip adersimizi:
HOST = socket.gethostbyname(socket.gethostname())
# print(socket.gethostname())
# print(HOST)
PORT = 12345 # rastgele bir port yazdım.

server_socket.bind((HOST, PORT))

server_socket.listen()

while True : 
    client_socket, client_address = server_socket.accept()
    print(f"Bağlantı yapıldı. {client_address}")
    print(client_socket ,client_address)

    client_socket.send("merhaba".encode("utf-8"))
    server_socket.close()
    
    break