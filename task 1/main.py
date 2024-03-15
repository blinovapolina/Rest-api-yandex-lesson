from flask import Flask
from data import db_session
from data.users import User
from data import db_session, jobs_api


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()