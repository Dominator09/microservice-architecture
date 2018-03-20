from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from controllers.usercontroller import UserService
import databaseConnection
databaseConnection.initialiseDatabase()

app = Flask(__name__)
api = Api(app)

api.add_resource(UserService,'/user')

if __name__ == '__main__':
    app.run(debug=True)
