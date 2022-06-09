import os
from django.shortcuts import redirect

from flask import Flask,flash, session, render_template,redirect, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
from helper import login_required
import datetime
import requests


load_dotenv()

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/iniciosecion" ,methods=["POST" , "GET"])
def inisiosecion():
    session.clear()
    if request.method == "POST":
        
        if not request.form.get("username"):
            flash("Llenar todos los campos")
            return render_template("iniciosecion.html")

        usuarios = request.form.get("username")
        #print(usuarios)
        
        if not request.form.get("password"):
            flash("Llenar todos los campos")
            return render_template("iniciosecion.html")

        password = request.form.get("password")
        #print(password)

        return redirect("/")
    else:
        return render_template("iniciosecion.html") 