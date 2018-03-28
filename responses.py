from flask_restful import fields, marshal_with,marshal
import json

def sendSuccess(data):
    output = {
        'statusCode': fields.Integer(default=200),
        'message': fields.String(default='Success'),
        'data':fields.Raw()
    }
    response = {
        'statusCode':200,
        'message':'Success',
        'data':{'access_token':data['data']}
    }
    return json.dumps(marshal(response,output))


def sendError(data):
    output = {
        'statusCode': fields.Integer(default=400),
        'message': fields.String(default='Error'),
        'data':{}
    }
    response = {
        'statusCode':400,
        'message':data['error'],
        'data':{}
    }
    return json.dumps(marshal(response,output))

        