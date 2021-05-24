from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@main.route('/login', methods=['GET'])
def login():
	return render_template('login.html')


@main.route('/home', methods=['GET'])
def home():
	return render_template('home.html')


@main.route('/ong/branch', methods=['GET'])
def ong():
	return render_template('ong_menu.html')


@main.route('/ong/branch/select', methods=['GET'])
def ong_select():
	return render_template('ong_select.html')


@main.route('/ong/branch/select/service', methods=['GET'])
def ong_service():
	return render_template('ong_service.html')


@main.route('/ong/professionals', methods=['GET'])
def ong_professionals():
	return render_template('ong_professionals.html')


@main.route('/ong/profile', methods=['GET'])
def ong_profile():
	pass


@main.route('/professional/profile', methods=['GET'])
def prof_profile():
	pass


@main.route('/professional/ongs', methods=['GET'])
def prof_ongs():
	pass
