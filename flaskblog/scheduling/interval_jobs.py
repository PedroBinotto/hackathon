from flaskblog import scheduler
from flaskblog.models import User


def manage_db():
    '''
    Remove usuários não confirmados da base de dados.
    '''
    with scheduler.app.app_context():
        users = User.query.all()
        for user in users:
            if not user.confirmed:
                db.session.delete(user)
