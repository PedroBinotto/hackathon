from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flaskblog import db
from flaskblog.models import Voluntario

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def home():
	return render_template('home.html')


@main.route('/ong', methods=['GET'])
def ong():
	pass
