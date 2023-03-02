import pymysql
#def getconn():
    #return pymysql.connect(host='database-1.cevwjjejgu87.ap-south-1.rds.amazonaws.com', database='IPL',user='admin',password='Tejas123')

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

def loginn(rqid):
    db=getconn()
    sql= "select passw from loguser where id=%d"
    cr=db.cursor()
    cr.execute(sql)
    pas=cr.fetchall()
    db.commit()
    db.close()
    return pas

def selectAllPass():
    db=getconn()
    sql='select * from loguser'
    cr=db.cursor()
    cr.execute(sql)
    el=cr.fetchall()
    db.commit()
    db.close()
    return el

def selectAllPlayer():
    db=getconn()
    sql='select * from master_table'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist








from flask import *
#from dbm import selectAllTeam , loginn, selectAllPlayer
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('Home_page.html')



@app.route("/about")
def about_super11():
    return render_template("About_super11.html")


@app.route("/team")
def team_list():
    el=selectAllTeam()
    return render_template("teams.html",elist=el)

@app.route("/log")
def login():
    return render_template("log.html")

@app.route("/player")
def player():
    pl=selectAllPlayer()
    return render_template("show.html",elist=pl)

@app.route("/loginn", methods=["GET","POST"])
def loguser():
    ep = selectAllPass()
    rqid=request.form.get('Team_id')
    repass=request.form.get('password')
    for i in range(3):
        ide = request.args.get['id']
        passw = request.args.get['passw']
        
        if (rqemail==ide and rqpassw==passw)in ep:
            return redirect("/")
        else:
            return "login fail"
    return redirect("/")
   



if(__name__=="__main__"):
    app.run(debug=True)
