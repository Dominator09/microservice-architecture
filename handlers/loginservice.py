from flask_restful import Resource, Api, reqparse, fields, marshal_with
import databaseConnection
import jwt
import constants
db = databaseConnection.getDatabaseInstance()

def login(data):
    try:
        cursor = db.cursor()
        if 'email' not in data or data['email'] is None:
            return {'error':'Email is Invalid'}

        sql = "SELECT user_id FROM tb_admin WHERE email = '%s'" % (data['email'])
        cursor.execute(sql)
        user = cursor.fetchone()
        if user is None:
            return {'error':'User not found'}
        
        if 'password' not in data and user.password != data['password']:
            return {'error':"Incorrect Password"}

        sql = "DELETE FROM tb_sessions WHERE user=%d"%(user['user_id'])
        cursor.execute(sql)
        sql = "INSERT INTO tb_session (user,user_type) VALUES (%d,%d)" % (user['user_id'],0)
        cursor.execute(sql)
        session_id = cursor.lastinsertid
        token_data = {'session_id':session_id,'user':user['user_id'],'userType':0}
        token = jwt.encode(token_data,constants.JWT_SECRET_TOKEN,algorithm='HS256')
        return {'data':{'access_token':token}}

        db.commit()
    except Exception:
        db.rollback()
        raise
        return {'error':"ERROR"}