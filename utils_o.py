def manage_package(in_cadena, sock):
    recibido = 0
    esperado = len(in_cadena)
    package_size = 16
    out_cadena = ''
    while recibido < esperado:
        sock.sendall(in_cadena[recibido:recibido+package_size-1].encode())
        data = sock.recv(package_size)
        aux = data.decode()
        recibido += len(data)
        out_cadena = f'{out_cadena}{aux}'
    return out_cadena

    