from flask import Blueprint, render_template, request

history_bp = Blueprint("history", __name__,url_prefix="/history")
flag = True
@history_bp.route("/", methods=["GET","POST"])
def history():

    global indice, flag

    lista_de_frutas = ["Banana","Maçã","Kiwi","Uvas"]

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
            if indice >= len(lista_de_frutas) + 1:
                pass
            else:
                indice += 1
                print(indice)





    return render_template("history.html", frutas = lista_de_frutas, index= indice) 
