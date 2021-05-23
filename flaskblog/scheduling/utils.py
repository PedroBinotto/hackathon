from flask import current_app, render_template, request, url_for
from flask_mail import Message
from flaskblog import db, mail


def send_frequency_reminder(user, subject, url):
	'''
	Envia o email de notificação para o usuário.
	Aceita título de disciplina e url para página de presença.
	'''

	msg = Message(
		subject,
		sender=current_app.config['MAIL_USERNAME'],
		recipients=[user.email]
	)

	msg.html = render_template(
		'emails/frequency_reminder.html',
		unsub_url='https://projeto-t4ss0.herokuapp.com/cancel',
		subject_name = subject,
		frequency_url=url
	)
	mail.send(msg)
   