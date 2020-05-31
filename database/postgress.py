from flask import Flask, render_template, request, session, logging, url_for, redirect,flash
import psycopg2
from passlib.hash import sha256_crypt

# Connect to the POSTGRES DB
con = psycopg2.connect(host="localhost",
                       database="users",
                       user="postgres",
                       password="Newyear#123",)

# Cursor
cur = con.cursor()

cur.execute("select * from public.users")

rows = cur.fetchall()

for r in rows:
    print(f"username {r[0]} password {r[1]}")

postgress = Flask(__name__)

@postgress.route('/')
def login():
    return render_template('login.html')

# @postgress.route('/login', methods=["GET","POST"])
# def login():
#     print(request.method)
#     if request.method == 'GET':
#         username = request.form.get("username")
#         password = request.form.get("password")
#         secure_password = sha256_crypt.encrypt(str(password))

#         usernamedata=cur.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
#         passworddata=cur.execute("SELECT password FROM users WHERE username=:username",{"username":username}).fetchone()

#         if usernamedata is None:
#             flash("Username not Found", "danger")
#             return render_template("login.html")
#         else:
#             for password_data in passworddata:
#                 if sha256_crypt.verify(password,password_data):
#                     flash("Login success", "success")
#                     return redirect(url_for('photo'))
#                 else:
#                     flash("Incorrect password","danger")
#                     return render_template("login.html")
    
#     return render_template("photo.html")
 
 #Photo
@postgress.route("/photo")
def photo():
    return render_template("photo.html")


if __name__ == '__main__':
    postgress.secret_key="Newyear#123"
    postgress.run(debug=True)

