import socket

IP="127.0.0.1"
PORT=20666
BFSize=512

if __name__ == '__main__':
    CliSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    Serv_loc=(IP,PORT)
    msj = "Hola, soy el cliente"
    msj_cli=str.encode(msj)

    CliSock.sendto(msj_cli, Serv_loc)   


    msj_serv=CliSock.recvfrom(BFSize)
    msj = "Servidor dice {}".format(msj_serv[0])
    print(msj)
