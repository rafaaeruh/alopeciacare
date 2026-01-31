from flask import Flask, Blueprint, render_template, request, current_app
from db.init_db import registrar_sessao
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
        pathsx = []
        paths = []

        for i,file in enumerate(arquivos):
            if file and file.filename != "":
                filename = names[i] + "_" + nowdata + ".jpg"
                upload_path = os.path.join(current_app.root_path ,"static", "uploads", filename) 
                pathsx.append(upload_path)
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


        for path in pathsx:
            url = path.split("/static")[-1]
            paths.append(url)

        try:
            registrar_sessao(data=nowdata,tratamento=tratamento,photo_frontal=paths[0],photo_entradas=paths[1],photo_midscalp=paths[2],photo_coroa=paths[3], frontal_estado=frontal,entradas_estado=entradas,midscalp_estado=mid_scalpr,coroa_estado=coroa, obs=observacao)
        except:
            print("Erro inesperado!")

    return  render_template("newsession.html")

