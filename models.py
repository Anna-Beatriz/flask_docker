# models.py

import datetime
from app import db


class Comentario(db.Model):
    __tablename__ = "comentarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    comentario = db.Column(db.String(200), nullable=False)
    data_com = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, email, comentario):
        self.nome = nome
        self.email = email
        self.comentario = comentario
        self.data_com = datetime.datetime.now()

    def __repr__(self):
        return "<Comentario %r>" % self.id
