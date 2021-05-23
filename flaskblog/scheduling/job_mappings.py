from flaskblog.scheduling.cron_jobs import email_users
from flaskblog.scheduling.interval_jobs import manage_db

cron_mappings = [
    {   # POO segunda-feira
        "func": email_users,
        "args": [
            'Programação Orientada à Objetos',
            'https://moodle.ufsc.br/mod/attendance/view.php?id=2559386'
        ],
        "trigger": 'cron',
        "day_of_week": 0,
        "hour": 18,
        "minute": 30,
        "timezone": 'Brazil/East',
        "id": 'monday1830'
    },
    {   # TGS terça-feira
        "func": email_users,
        "args": [
            'Teoria Geral de Sistemas',
            'https://moodle.ufsc.br/mod/attendance/view.php?id=2618330'
        ],
        "trigger": 'cron',
        "day_of_week": 1,
        "hour": 22,
        "minute": 0,
        "timezone": 'Brazil/East',
        "id": 'tuesday2200'
    },
    {   # POO quarta-feira
        "func": email_users,
        "args": [
            'Programação Orientada à Objetos',
            'https://moodle.ufsc.br/mod/attendance/view.php?id=2559386'

        ],
        "trigger": 'cron',
        "day_of_week": 2,
        "hour": 18,
        "minute": 30,
        "timezone": 'Brazil/East',
        "id": 'wednesday1830'
    },
    {   # Inf quarta-feira
        "func": email_users,
        "args": [
            'Introdução à Informática',
            'https://moodle.ufsc.br/mod/attendance/view.php?id=2570023'
        ],
        "trigger": 'cron',
        "day_of_week": 2,
        "hour": 20,
        "minute": 20,
        "timezone": 'Brazil/East',
        "id": 'wednesday2020'
    },
    {   # Inf sexta-feira
        "func": email_users,
        "args": [
            'Introdução à Informática',
            'https://moodle.ufsc.br/mod/attendance/view.php?id=2570023'
        ],
        "trigger": 'cron',
        "day_of_week": 4,
        "hour": 20,
        "minute": 20,
        "timezone": 'Brazil/East',
        "id": 'friday2020'
    }
]

interval_mappings = [
    {
        "func": manage_db,
        "trigger": 'interval',
        "minutes": 60,
        "id": 'database'
    }
]
