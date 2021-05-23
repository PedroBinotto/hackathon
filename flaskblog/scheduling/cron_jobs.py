from flaskblog import scheduler
from flaskblog.models import User
from flaskblog.scheduling.utils import send_frequency_reminder


def email_users(subject, url):
    '''
    Notifica todos os usuários confirmados da base de dados com base em
    disciplina e url (presença).
    '''
    with scheduler.app.app_context():
        users = User.query.all()
        for user in users:
            if user.confirmed:
                send_frequency_reminder(
                    user,
                    subject,
                    url
                )
