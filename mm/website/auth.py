from crypt import methods
from xmlrpc.client import boolean
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login', method=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up")
