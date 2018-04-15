from flask_restful import Resource, Api, reqparse, fields, marshal_with
import databaseConnection
import jwt
import constants
db = databaseConnection.getDatabaseInstance()

def getUser(email):
    cursor = db.cursor()
    if(email):
        query = "SELECT * FROM tb_admin WHERE email='%s'" % (email)
        cursor.execute(query)
        result = cursor.fetchone()
        print("################RES#######################",result)
        return result

    else:
        query = "SELECT * FROM tb_admin"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def putUser(user_detail):
    try:
        cursor = db.cursor()
        check_user_query = "SELECT user_id FROM tb_admin WHERE email='%s'" % (user_detail['email'])
        cursor.execute(check_user_query)
        result = cursor.fetchone()
        if(result):
            return {'error':"User Alread Exists",'data':None}

        sql = "INSERT INTO tb_admin (email,password,first_name,last_name,phone_no) VALUES ('%s','%s','%s','%s','%s')"
              % (user_detail['email'],user_detail['password'],user_detail['first_name'],user_detail['last_name'],user_detail['phone_no'])
        print(sql)
        result = cursor.execute(sql)
        user_id=cursor.lastrowid
        session = "INSERT INTO tb_session (user,user_type) VALUES (%d,%d,%d,'%s')"
              % (user_id,0,user_detail['device_type'],user_detail['device_token'])
        cursor.execute(session)
        session_id = cursor.lastrowid
        token_data = {'session_id':session_id,'user':user_id,'userType':0}
        token = jwt.encode(token_data,constants.JWT_SECRET_TOKEN,algorithm='HS256')

        db.commit()
        return {'data':token}  
         
    except Exception:
        db.rollback()
        raise
        return {},400
