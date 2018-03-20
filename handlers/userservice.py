from flask_restful import Resource, Api, reqparse, fields, marshal_with
import databaseConnection
import jwt

db = databaseConnection.getDatabaseInstance()

def getUser(email):
    cursor = db.cursor()
    if(email):
        query = "SELECT * FROM tb_admin WHERE email='%s'" % (email)
        cursor.execute(query)
        result = cursor.fetchone()
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
        print("#########################",cursor.fetchone())
        if(cursor.fetchone()):
            return "User already Exists"

        sql = "INSERT INTO tb_admin (email,password) VALUES ('%s','%s')" % (email,password)
        print(sql)
        result = cursor.execute(sql)
        print("INSERT RESULT######################",result)
        session = "INSERT INTO tb_session (user,user_type) VALUES (%d,%d)" % (1,0)
        print("SESSION######################3",session)
        cursor.execute(session)
        db.commit()
        return result  
         
    except:
        db.rollback()
        return {},400
