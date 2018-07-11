from flask_restful import Resource,reqparse, fields, marshal_with
from handlers import userservice,loginservice
import json,responses,requestParsers
from utilities import identity
from handlers.storageService import Storage



class StorageService(Resource):
    def post(self):
        parser = requestParsers.createStorage()
        args = parser.parse_args()
        user = identity.verifySession(args)
        if 'error' in user:
            return responses.sendError(user)

        newStore = Storage(args['name'],args['size'])
        result = newStore.createDrive(args['name'],args['size'],1)
        if(result['error']):
            responses.sendError(result)
        else:
            responses.sendSuccess(result)   

            

                          

        


