import socket

IP="127.0.0.1"
PORT=20666
BFSize=512

if __name__ == '__main__':
    msj="Bienvenido cliente"
    btsend=str.encode(msj)
    SerSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    SerSock.bind((IP, PORT))
    print "Servidor activo y listo"
    msj="Hola cliente"
    fin=False
    while not fin:
        btrec = SerSock.recvfrom(BFSize)
        msg_ent = btrec[0]
        dir_ent = btrec[1]
        cli_Msg = "Mensaje cliente:{}".format(msg_ent)
        cli_IP  = "Ip cliente:{}".format(dir_ent)
        print(cli_Msg)
        print(cli_IP)
        msj_serv=str.encode(msj)
        SerSock.sendto(msj_serv, dir_ent)
