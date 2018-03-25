from flask_restful import Resource, Api, reqparse, fields, marshal_with,marshal
from handlers import userservice
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
        return result