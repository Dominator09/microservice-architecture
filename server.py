from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from controllers.usercontroller import UserService,LoginService
import databaseConnection,tcpSockets

from utilities import signal

databaseConnection.initialiseDatabase()
tcpSockets.initiate_tcp_server()

app = Flask(__name__)
api = Api(app)

api.add_resource(UserService,'/register')
api.add_resource(LoginService,'/login')
if __name__ == '__main__':
    app.run(debug=True)
