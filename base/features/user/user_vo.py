import uuid
from datetime import datetime

from sqlalchemy import Integer, String

from base import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', String(36), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column('email', String(255), nullable=False, unique=True)
    password = db.Column('password', String(255), nullable=False)
    full_name = db.Column('full_name', String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        db.create_all()
