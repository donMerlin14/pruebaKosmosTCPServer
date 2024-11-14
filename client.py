import socket
import sys

# Creando socket TPC/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando con el servidor
server_address = ('localhost', 5000)
sock.connect(server_address)
print('Hola servidor')
try:
    while True:
        lower_input = input("Ingresa tu mensaje \n")
        if lower_input == "DESCONEXION":
            sock.sendall(lower_input.encode())
            break
        else:
            sock.sendall(lower_input.encode())
            upper_out = sock.recv(16)
            out_str = upper_out.decode()
            print(out_str)
finally:
    print('Adios servidor')
    sock.close()