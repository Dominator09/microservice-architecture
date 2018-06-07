import socket
import subprocess
from multiprocessing import Process

class TcpSocket:
    tcp_socket = 0
    def __init__(self):
        tcp_socket = {'close':self.commodity}

    @classmethod
    def get_tcp_connection_instance(cls):
        return cls.tcp_socket

        
    def commodity(self):
        return
    
    def getFreePort(self,start_range,end_range):
        if(start_range < 1023):
            return {'error':'SYSTEM services port cannot be user'}
    
        if(end_range > 65535):
            return {'Not a valid 16-bit tcp port'}
    
        else:
            return start_range    
    
    
    def add_to_process_queue(self,*fns):
        for fn in fns:
            new_process = Process(fn)
            new_process.start()
            new_process.join()
    
    
    def handle_tcp_request(self,con,address):
            stream_input = con.recv(1024)
            print("#################Input##############",stream_input)
            con.close()
        
    def initiate_tcp_server(self):
        tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = socket.gethostname()
        port = self.getFreePort(2045,3000)
    
        tcp_socket.bind((host,port))
        tcp_socket.listen(5)
        while True:
            connection,address = tcp_socket.accept()
            print('got connection from',address)
            self.add_to_process_queue(self.handle_tcp_request(connection,address))
    
    






