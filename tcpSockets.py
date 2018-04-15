import socket
import subprocess
from multiprocessing import Process


def commodity():
    return

tcp_socket = {'close':commodity} 

def getFreePort(start_range,end_range):
    if(start_range < 1023):
        return {'error':'SYSTEM services port cannot be user'}

    if(end_range > 65535):
        return {'Not a valid 16-bit tcp port'}

    else:
        return start_range    


def get_tcp_connection_instance():
    return tcp_socket

 
def add_to_process_queue(*fns):
    for fn in fns:
        new_process = Process(fn)
        new_process.start()
        new_process.join()


def handle_tcp_request(con,address):
        stream_input = con.recv(1024)
        print("#################Input##############",stream_input)
        con.close()
    
def initiate_tcp_server():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = getFreePort(2045,3000)

    tcp_socket.bind((host,port))
    tcp_socket.listen(5)
    while True:
        connection,address = tcp_socket.accept()
        print('got connection from',address)
        add_to_process_queue(handle_tcp_request(connection,address))








