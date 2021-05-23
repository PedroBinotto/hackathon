from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def home():
	return render_template('home.html')


@main.route('/ong', methods=['GET'])
def ong():
	pass
