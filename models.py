from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import validates, relationship, backref, joinedload

from datetime import datetime
# from flask_marshmallow import Marshmallow

db = SQLAlchemy()
# ma = Marshmallow()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):

        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class User(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'users'

    id            = db.Column(db.Integer, primary_key = True)
    name          = db.Column(db.String(250), nullable=False)

    cpf           = db.Column(db.String(9), nullable=False)
    email         = db.Column(db.String(120), nullable=False, unique=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())
    visits = db.relationship("Visit", lazy='select', backref=db.backref('user', lazy='joined'), cascade="all, delete-orphan")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Visit(BaseModel, db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

