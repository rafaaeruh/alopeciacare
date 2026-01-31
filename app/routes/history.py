from flask import Blueprint, render_template, request
from db.init_db import buscar_history


history_bp = Blueprint("history", __name__,url_prefix="/history")
flag = True
@history_bp.route("/", methods=["GET","POST"])
def history():

    global indice, flag

    sessoes_lista = buscar_history()


    if flag:
        indice = 3

    if request.method == "POST":

        if request.form.get("acao") == "esq":
            if indice <= 3:
                pass
            else:
                flag = False
                indice -= 1
                print(indice)
        elif request.form.get("acao") == "dir" :
            if indice >= len(sessoes_lista) + 1:
                pass
            else:
                indice += 1
                print(indice)

    return render_template("history.html", sessoes = sessoes_lista, index= indice) 
