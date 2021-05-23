from datetime import datetime

from flaskblog import db


class Voluntario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(50), nullable=False)

class Organizacao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(50), nullable=False)
