from flask import Flask, render_template,redirect,url_for, request
from flask_login import LoginManager, UserMixin, login_user,login_required,logout_user,current_user
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self,id):
        self.id = id

users = {'1':{'username':'shriyugag','password':'12345678'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def taskList():
    return render_template("login.html")

@app.route("/list")
def login():
    return render_template("index.html")

@app.route("/auth",methods=["POST"])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    user_id=None
    for uid,user in users.items():
        if user['username'] == username and user['password']==password:
            user_id = uid
            break
    if user_id:
        user = User(user_id)
        login_user(user)
        return redirect(url_for('login'))
    else:
        return "Invalid username or password"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('taskList'))


app.run(debug=True)
