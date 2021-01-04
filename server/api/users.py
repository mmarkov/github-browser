# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api, Resource
from models import User
from flask.globals import request
from flask import current_app


users_api = Api(Blueprint('users_api', __name__))

PER_PAGE = 25


@users_api.resource('/users')
class UsersAPI(Resource):
    @staticmethod
    def get():
        page = request.args.get('page', default=1)
        try:
            page = int(page)
        except ValueError:
            page = 1
        users_query = User.query.paginate(page, PER_PAGE)
        result = {
            'pages': {
                'current': users_query.page,
                'total': users_query.pages,
                'has_next': users_query.has_next,
                'has_prev': users_query.has_prev,
                'next_num': users_query.next_num,
                'prev_num': users_query.prev_num,
            },
            'users': [{
                'id': user.id,
                'login': user.login,
                'name': user.name,
                'avatar_url': user.avatar_url,
                'html_url': user.html_url,
                'user_type': user.user_type,
                'twitter_username': user.twitter_username,
            } for user in users_query.items],
        }
        return result
