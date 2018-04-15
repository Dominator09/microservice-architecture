from flask_restful import Resource, Api, reqparse, fields, marshal_with,marshal
from handlers import userservice,loginservice
import json,responses,requestParsers,identity


class UserService(Resource):

    def get(self):
        parser = requestParsers.getUserParser()
        args = parser.parse_args()
        user = identity.verifySession(args)
        if 'error' in user:
            return responses.sendError(user)

        args['user'] = user['data']    
        result = userservice.getUser(args.email)
        if('data' in result):
            return responses.sendSuccess(result)
        else:
            return responses.sendError(result)
          
 
    def put(self):
        parser = requestParsers.registerUser()
        args = parser.parse_args(strict=True)
        print(args)
        result = userservice.putUser(args)
        if('data' in result and result['data']):
            return responses.sendSuccess(result)
        else:
            return responses.sendError(result)
        
        
class LoginService(Resource):
    def post(self):
        parser = requestParsers.login()
        args = parser.parse_args()
        data = loginservice.login(args)
        if 'data' in data and data['data']:
           return responses.sendSuccess(data)
        else:
           return responses.sendError(data)