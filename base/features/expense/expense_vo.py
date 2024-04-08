import uuid
from datetime import datetime

from sqlalchemy import Integer, String, Float, ForeignKey, event

from base import db
from base.features.user.user_vo import User


class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column('id', String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    remark = db.Column('remark', String(255), nullable=False)
    quantity = db.Column('quantity', Integer, nullable=False)
    price = db.Column('price', Float, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column('user_id', String(36),
                        ForeignKey(User.id, ondelete='CASCADE', onupdate='CASCADE'),
                        nullable=False)

    def __init__(self):
        db.create_all()
