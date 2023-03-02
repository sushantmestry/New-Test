import pymysql
def getconn():
    return pymysql.connect(host='localhost',database='IPL',user='root',passwd='')


def selectAllTeam():
    db=getconn()
    sql='select * from teams'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def loginn():
    db=getconn()
    sql= "select passw=%s from teams where id=%"
    cr=db.cursor()
    cr.execute(sql)
    db.commit()
    db.close()

def selectAllPlayer():
    db=getconn()
    sql='select * from master_table'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist


