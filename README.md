# pruebaKosmosTCPServer
servidor TPC básico que convierte frases a mayuscula

# instrucciones
Abrir dos lineas de comando separadas apuntando a la ruta donde se encuentran ambos archivos: server.py y client.py
En una jecutar el servidor utilizando el comando python .\server.py
La consola debe mostrar el mensaje "Esperando cliente"
En la segunda ejecutar el cliente utilizando el comando python .\client.py
La consola del cliente nos solicitará un mensaje hasta escribir la palabra exacta DESCONEXION
Ejemplo:

Cliente                         Servidor
                                esperando cliente
Hola servidor                   
                                HOLA CLIENTE
ingresa tu mensaje
    -oso
    OSO
ingresa tu mensaje
    -DESCONEXION
    Adios servidor             
                                adios cliente
                                esperando cliente