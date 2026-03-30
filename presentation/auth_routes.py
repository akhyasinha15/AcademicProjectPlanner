from flask import Blueprint, render_template, request, redirect
from data.models import User
from data.db import db

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            return redirect("/dashboard")

    return render_template("login.html")