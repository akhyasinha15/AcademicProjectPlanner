from flask import Blueprint, render_template, request, redirect, session

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/dashboard")

    return render_template("login.html")

