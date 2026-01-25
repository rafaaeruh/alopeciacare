#classe Python  que representa a aplicação web
from flask import Flask
from routes.history import history_bp

# Instância da classe que represente a aplicação web
app = Flask(__name__)

app.register_blueprint(history_bp)

@app.route("/")
def home():
    return 'app rodandoo :D'

if __name__ == "__main__":
    app.run(debug=True)


