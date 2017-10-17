import sqlite3
import os
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from init import db

class Calculator(db.Model):
    __tablename__ = 'weather_info'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80))
    date = db.Column(db.String(120))
    weather = db.Column(db.String(120))
    wind = db.Column(db.String(120))
    temperature = db.Column(db.String(120))
    last_updated_on = db.Column(db.String(120))
    queried_by = db.Column(db.String(120))

    def __init__(self, items):
        self.city = items['city']
        self.date = items['date']
        self.weather = items['weather']
        self.wind = items['wind']
        self.temperature = items['temperature']
        self.last_updated_on = items['last_updated_on']
        self.queried_by = items['queried_by']

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def as_dict(self):
       return {col.name: getattr(self, col.name) for col in self.__table__.columns}

db.drop_all()
db.create_all()
