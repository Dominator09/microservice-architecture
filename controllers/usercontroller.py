from flask_restful import Resource, Api, reqparse, fields, marshal_with,marshal
from handlers import userservice,loginservice
import json

output = {
    'statusCode': fields.Integer(default=200),
    'message': fields.String(default='Success'),
    'data':fields.Raw()
}
class UserService(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        args = parser.parse_args()
        result = userservice.getUser(args.email)
        print("############DICT###########",result)
        response = {}
        if(result):
            response = {
                'statusCode':200,
                'message':'Success',
                'data':result
            }
        else:
          response = {
                'statusCode':400,
                'message':'Not Found',
                'data':{},
            }
        
        print(result)
        return json.dumps(marshal(response,output))
          
 
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',required=True,help="Email is requirerd")
        parser.add_argument('password')
        args = parser.parse_args(strict=True)
        print(args)
        result = userservice.putUser(args.email,args.password)
        if(result['data']):
            response = {
                'statusCode':200,
                'message':'Success',
                'data':{'access_token':result['data']}
            }
        else:
          response = {
                'statusCode':400,
                'message':result['error'],
                'data':{},
            }

        return json.dumps(marshal(response,output))

class LoginService(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        parser.add_argument('password')
        args = parser.parse_args()
        data = loginservice.login(args)
        if 'data' in data and data['data']:
            response = {
                'statusCode':200,
                'message':'Success',
                'data':{'access_token':data['data']}
            }
        else:
          response = {
                'statusCode':400,
                'message':data['error'],
                'data':{},
            }

        return json.dumps(marshal(response,output))
