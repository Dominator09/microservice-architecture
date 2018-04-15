import signal,os
import tcpSockets

def termination_handler():
    socket = tcpSockets.get_tcp_connection_instance()
    socket.close()
    return

    