import socket
import sys

# Creando socket TPC/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Iniciando el socket en localhost puerto 5000
server_address = ('localhost', 5000)
print('Iniciando servidor en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Escuchando conexiones
sock.listen(1)

while True:
    # Esperando una conexión
    print('esperando cliente')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Recibiendo datos desde la conexión
        while True:
            data = connection.recv(16)
            str_data = data.decode()
            if str_data:
                if str_data == "DESCONEXION":
                    print('desconectando...')
                    break
                else:
                    upper_data = data.upper()
                    connection.sendall(upper_data)
    finally:
        # Cerrando la conexión
        print('Cerrnado conexión')
        connection.close()