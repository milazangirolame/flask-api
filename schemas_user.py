from ma import ma
from models.model import User
from marshmallow import fields, validate

class UserSchema(ma.ModelSchema):

    id            = db.Column(db.Integer, primary_key = True)
    name          = db.Column(db.String(250), nullable=False, required=True, validate=[validate.Length(min=2)])

    cpf           = db.Column(db.String(250), nullable=False, required=True, validate=[validate.Length(min=9)])
    email         = db.Column(db.String(100), unique=True, required=True, validate=[validate.Length(min=2)])
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())
    visits = relationship("Visit", cascade="all, delete-orphan")



    class Meta:
        model = User
