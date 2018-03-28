import databaseConnection
import jwt
import constants

def verifySession(session):
    db = databaseConnection.getDatabaseInstance()
    cursor = db.cursor()
    if('access_token' in session):
        decoded_data = jwt.decode(session['access_token'], constants.JWT_SECRET_TOKEN, algorithms=['HS256'])
        if('session_id' in decoded_data and 'user' in decoded_data):
            session_id = decoded_data['session_id']
            user = decoded_data['user']
            sql = "SELECT session_id FROM tb_sessions WHERE session_id=%d AND user=%d" % (session_id,user)
            cursor.execute(sql)
            session_data = cursor.fetchone()
            if(session_data):
                return {'data':session_data}
            else:
                return {'error':"Session Expired"}
        else:
            return {'error':"Session Expired"}
    else:
        return {'error':"Invalid Access Token"}


