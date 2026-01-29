from flask import Flask, Blueprint, render_template, request
import datetime
import os 


session_bp = Blueprint("session", __name__,url_prefix="/newsession")

@session_bp.route("/", methods=["GET","POST"])
def session():

    nowdata = datetime.datetime.now().strftime("%Y/%m/%d").replace("/", "-")
    
    if request.method == "POST":

        # FOTOS
        file1 = request.files["photo_frontal"]
        file2 = request.files["photo_entradas"]
        file3 = request.files["photo_midscalp"]
        file4 = request.files["photo_coroa"]
        arquivos = [file1,file2,file3,file4]
        names = ["frontal","entradas","mid_scalp","coroa"]
        paths = []


        for i,file in enumerate(arquivos):
            if file and file.filename != "":
                filename = names[i] + "_" + nowdata + ".jpg"
                upload_path = os.path.join("static", "uploads", filename) 
                paths.append(upload_path)
                file.save(upload_path)

        # Formula

        tratamento = request.form.get("formula")

        # Estado

        frontal = request.form.get("frontalr")
        entradas = request.form.get("entradasr")
        mid_scalpr = request.form.get("mid_scalpr")
        coroa = request.form.get("coroar")

        #obs

        observacao = request.form.get("obs")




        print (tratamento, frontal,entradas,mid_scalpr,coroa, observacao, nowdata)
            



    return  render_template("newsession.html")

