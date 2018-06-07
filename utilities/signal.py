import signal,os
from tcpSockets import TcpSocket
def termination_handler():
    socket = TcpSocket.get_tcp_connection_instance()
    socket.close()
    return

    