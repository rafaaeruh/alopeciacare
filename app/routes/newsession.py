from flask import Flask, Blueprint, render_template, request
import datetime
import os 


session_bp = Blueprint("session", __name__,url_prefix="/newsession")

@session_bp.route("/", methods=["GET","POST"])
def session():

    nowdata = datetime.datetime.now().strftime("%Y/%m/%d").replace("/", "-")
    
    if request.method == "POST":
        file1 = request.files["photo_frontal"]
        file2 = request.files["photo_entradas"]
        file3 = request.files["photo_midscalp"]
        file4 = request.files["photo_coroa"]
        arquivos = [file1,file2,file3,file4]
        names = ["frontal","entradas","mid_scalp","coroa"]

        for i,file in enumerate(arquivos):
            if file and file.filename != "":
                filename = names[i] + "_" + nowdata + ".jpg"
                upload_path = os.path.join("static", "uploads", filename) 
                file.save(upload_path)

    return  render_template("newsession.html")

