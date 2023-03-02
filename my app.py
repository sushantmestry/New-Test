from flask import *
from dbm import selectAllTeam , loginn, selectAllPlayer
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
    el = selectAllTeam()
    rqid=request.form.get('id')
    rqpassw = request.form.get('password')
    for i in range(4):
        ide = request.args.get('id')
        passw = request.args.get('passw')
        
        if (rqid==ide and rqpassw==passw)in el:
            return redirect("/")
        else:
            return redirect("/team")
    return redirect("/")



if(__name__=="__main__"):
    app.run(debug=True)
