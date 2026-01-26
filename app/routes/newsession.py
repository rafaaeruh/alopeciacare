from flask import Flask, Blueprint, render_template

session_bp = Blueprint("session", __name__,url_prefix="/newsession")

@session_bp.route("/")
def session():
    return  render_template("newsession.html")