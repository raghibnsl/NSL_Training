from flask import Blueprint, render_template, request, flash,redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash



auth=Blueprint('auth',__name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    data=request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method=="POST":
        email=request.form.get('email')
        firstname=request.form.get('firstName')
        password1=request.form.get('password3')
        password2=request.form.get('password4')
        if len(email)<10:
            flash("Email is too short", category="error")
        elif " " in email:
            flash("Avoid using blankspaces in emails",category='error')
        elif len(password1)<8:
            flash("The password must be atleast of 8 characters in length", category='error')
        elif password2!=password1:
            flash("Sorry your passwords dont match",category="error")
        else:
            new_user=User(email=email,password=generate_password_hash(password1,method='sha256'),first_name=firstname)
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!",category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")