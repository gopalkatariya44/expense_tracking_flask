import uuid
from datetime import datetime

from sqlalchemy import Integer, String, Float, ForeignKey, event

from base import db
from base.features.user.user_vo import User


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column('id', String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column('name', String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column('user_id', String(36),
                        ForeignKey(User.id, ondelete='CASCADE', onupdate='CASCADE'),
                        nullable=False)

    def __init__(self):
        db.create_all()
