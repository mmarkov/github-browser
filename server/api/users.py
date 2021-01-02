# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api, Resource
from models import User
from flask.globals import request
from flask import current_app


users_api = Api(Blueprint('users_api', __name__))


@users_api.resource('/users')
class UsersAPI(Resource):
    @staticmethod
    def get():
        page = request.args.get('page', 1)
        current_app.logger.info("page %s" % page)
        users = User.query
        current_app.logger.info("users %s" % users)
        return [{
            'id': user.id,
            'login': user.login
        } for user in users]
        # jsonify(json_list = qryresult.all())
