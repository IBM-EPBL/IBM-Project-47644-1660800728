from flask import *
import pandas
#Flask,render_template,redirect,request
import sqlite3

db = sqlite3.connect('database.db')
app = Flask(__name__)
cursor = db.cursor()
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("/home.html")

@app.route("/login_validation",methods=["POST","GET"])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    df=pandas.read_csv(f"{email}.csv")
    d = df.to_dict()
    f = d[email]
    if f[0] == email:
        if f[1]==password:
            return redirect(url_for("home"))
        else:
            return "wrong password"
    else:
        return "username or password wrong"
@app.route("/signup",methods=["POST","GET"])
def signup():
    name = request.form.get("name")
    email = request.form.get('email')
    password = request.form.get('password')
    if len(name)>0:
        dt = pandas.DataFrame({email: [email, password]})
        dt.to_csv(f"{email}.csv")
        df = pandas.read_csv(f"{email}.csv")
        d = df.to_dict()
        print(d[email])
        return redirect(url_for("login"))
    else:
        return "press go back and please fill the name"

if __name__=="__main__":
    app.run(debug=True)
