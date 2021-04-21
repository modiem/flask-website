from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        pass


    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>logout</pi>"

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif len(email) < 4:
            flash("Email address must be larger than 3 characters", category="error")
        elif len(password1) < 7:
            flash("Password must at least 7 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        # else:
            # add to data base
    return render_template("sign_up.html")