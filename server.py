from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from controllers.usercontroller import UserService,LoginService
import databaseConnection
from tcpSockets import TcpSocket

from utilities import signal

databaseConnection.initialiseDatabase()
tcp_socket = TcpSocket()
tcp_socket.initiate_tcp_server()


app = Flask(__name__)
api = Api(app)

api.add_resource(UserService,'/register')
api.add_resource(LoginService,'/login')

if __name__ == '__main__':
    app.run(debug=True)
