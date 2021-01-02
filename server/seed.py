import os
from flask_script import Command, Option
from flask_sqlalchemy import SQLAlchemy

from github import Github
from models import User


class SeedCommand(Command):
    """Download list of users from github and store them locally"""

    WRITE_BATCH = 25
    """Number of records committed to database in single batch"""

    DEFAULT_USER_COUNT = 150
    """Default number of users to download from Github"""

    DEFAULT_PER_PAGE = 100
    """Number of records requested from Github at once"""

    def get_options(self):
        return [
            Option(
                '-t',
                '--total',
                dest='count',
                default=SeedCommand.DEFAULT_USER_COUNT,
                help="number of users to download from GitHub (default 150)"),
        ]

    def run(self, count: str) -> None:
        user_count = SeedCommand.DEFAULT_USER_COUNT
        try:
            user_count = int(count)
        except ValueError:
            print("Please provide number of users to download as valid int")
            exit(1)

        db_engine = self.__init_db()
        # users API is publicly available, but token helps to lift throttling limits
        token = None
        if 'GITHUB_TOKEN' in os.environ:
            token = os.environ['GITHUB_TOKEN']
        gh = Github(login_or_token=token, per_page=SeedCommand.DEFAULT_PER_PAGE)
        self.__download_users(db_engine, gh, user_count)

    @staticmethod
    def __init_db() -> SQLAlchemy:
        from flask import _request_ctx_stack
        from app import db
        app = _request_ctx_stack.top.app
        db.init_app(app)

        with app.app_context():
            db.drop_all()
            db.create_all()

        return db

    def __download_users(self, db: SQLAlchemy, gh: Github, count: int) -> None:
        github_users = gh.get_users()
        for index, github_user in enumerate(github_users):
            user = self.__create_user(github_user)
            # TODO move SQLLite operations to async
            db.session.add(user)
            if (index + 1) % SeedCommand.WRITE_BATCH == 0:
                db.session.commit()
            if index + 1 >= count:
                db.session.commit()
                break

    @staticmethod
    def __create_user(github_user):
        user = User()
        user.id = github_user.id
        user.login = github_user.login
        user.avatar_url = github_user.avatar_url
        user.user_type = github_user.type
        user.html_url = github_user.html_url
        user.name = github_user.name
        user.public_repos = github_user.public_repos
        user.twitter_username = github_user.twitter_username
        user.location = github_user.location
        return user
