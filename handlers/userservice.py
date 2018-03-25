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

def putUser(email,password):
    try:
        cursor = db.cursor()
        check_user_query = "SELECT user_id FROM tb_admin WHERE email='%s'" % (email)
        cursor.execute(check_user_query)
        result = cursor.fetchone()
        print("#########################",cursor.fetchone())
        if(result):
            return "User already Exists"

        sql = "INSERT INTO tb_admin (email,password) VALUES ('%s','%s')" % (email,password)
        print(sql)
        result = cursor.execute(sql)
        print("INSERT RESULT######################",result,cursor.lastrowid)
        user_id=cursor.lastrowid
        session = "INSERT INTO tb_session (user,user_type) VALUES (%d,%d)" % (user_id,0)
        print("SESSION######################3",session)
        cursor.execute(session)
        session_id = cursor.lastrowid
        token_data = {'session_id':session_id,'user':user_id,'userType':0}
        token = jwt.encode(token_data,constants.JWT_SECRET_TOKEN,algorithm='HS256')

        db.commit()
        return token  
         
    except Exception:
        db.rollback()
        raise
        return {},400
