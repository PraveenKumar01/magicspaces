from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
import psycopg2
from passlib.hash import sha256_crypt

# Connect to the POSTGRES DB
con = psycopg2.connect(host="localhost",
                       database="users",
                       user="postgres",
                       password="Newyear#123",)

# Cursor
cur = con.cursor()

cur.execute("select * from public.quickbits")

rows = cur.fetchall()

# for r in rows:
#     print(f"username {r[0]} password {r[1]}")

postgress = Flask(__name__)


@postgress.route('/')
def home():

    return render_template("login.html")


@postgress.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":

        fusername = request.form.get("username")

        fpassword = request.form.get("password")

        print(fusername)

        print(fpassword)

        cur.execute("select * from public.registration WHERE username=%s", (fusername,))

        row = cur.fetchone()

        db_Username = row[1]
        print(db_Username)

        db_Password = row[2]

        print(db_Password)

        db_clientid = row[3]

        print(db_clientid)

        cur.execute(
            "select image from public.quickbits WHERE clientid=%s", (db_clientid,))

        img = cur.fetchall()

        # arr_img = str(db_Image).split(';')

        if db_Username is None:

            # print("Username")

            flash("Username not Found", "danger")

            return render_template("login.html")
        else:

            if fpassword == db_Password:

                # session['user_name'] = fusername

                # temp = str(fusername)
                # cur.execute("select image from public.users WHERE username=username",fusername)

                # img =cur.fetchone()

                # arr_img = str(img).split(';')

                # print(arr_img)

                # session['arr_img'] = arr_img

                flash("Login success", "success")

                return render_template("photo.html", temp=fusername, arrimage=img)

            else:
                print('incorrectpass')

                print(fusername)

                print(db_Password)

                flash("Incorrect password", "danger")

                return render_template("login.html")

        # return render_template("photo.html")
    else:
        return "test"

 # Photo


@ postgress.route("/photo")
def photo():
    return render_template("photo.html")


if __name__ == '__main__':
    postgress.secret_key = "Newyear#123"
    postgress.run(debug=True)
