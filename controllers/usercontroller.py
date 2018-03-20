from flask_restful import Resource, Api, reqparse, fields, marshal_with
from handlers import userservice

class UserService(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        args = parser.parse_args()
        result = userservice.getUser(args.email)
        print(result)
        return result  
 
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',required=True,help="Email is requirerd")
        parser.add_argument('password')
        args = parser.parse_args(strict=True)
        print(args)
        result = userservice.putUser(args.email,args.password)
        return result