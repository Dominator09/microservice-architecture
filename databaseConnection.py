import MySQLdb
import MySQLdb.cursors
from multiprocessing import Process

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


def initialiseDatabase():
    print("IN HERE")
    db = MySQLdb.connect('localhost','root','elnino','pythonDB',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    print(db)
    query = "CREATE TABLE IF NOT EXISTS `tb_admin` ("\
            " user_id INT AUTO_INCREMENT, "\
            " email varchar(100) NOT NULL, "\
            " password varchar(500) NOT NULL,"\
            " PRIMARY KEY (user_id)"\
            ");"

    query2 = "CREATE TABLE IF NOT EXISTS `tb_session` ("\
            " session_id INT AUTO_INCREMENT, "\
            " user_type INT NOT NULL, "\
            " user INT NOT NULL,"\
            " PRIMARY KEY (session_id)"\
            ");"
    try:
        print(query,query2)
        runInParallel(cursor.execute(query),cursor.execute(query2))
        db.commit()
    except:
        db.rollback()


def getDatabaseInstance():
    db = MySQLdb.connect('localhost','root','elnino','pythonDB',cursorclass=MySQLdb.cursors.DictCursor)
    return db
