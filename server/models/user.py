# -*- coding: utf-8 -*-
from datetime import datetime
from app import db


class User(db.Model):
    """Model for Github user"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    login = db.Column(db.String, nullable=False)
    avatar_url = db.Column(db.String)
    user_type = db.Column(db.String)
    html_url = db.Column(db.String)
    name = db.Column(db.String)
    public_repos = db.Column(db.Integer)
    twitter_username = db.Column(db.String)
    location = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)
