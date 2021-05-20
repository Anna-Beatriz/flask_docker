# app.py

import os
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        comentario = request.form['comentario']
        coment = Comentario(nome, email, comentario)
        db.session.add(coment)
        db.session.commit()
    comentarios = Comentario.query.order_by(Comentario.data_com.desc()).all()
    return render_template('index.html', comentarios=comentarios)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
