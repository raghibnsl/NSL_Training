from flask import Blueprint, render_template, request
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
        first_name=request.form.get('firstName')
        password1=request.form.get('password3')
        password2=request.form.get('password4')
        print(email,first_name,password1, password2)
    return render_template("signup.html")