import uuid
from datetime import datetime

from sqlalchemy import Integer, String, Float, ForeignKey, event
from sqlalchemy.orm.attributes import set_committed_value

from base import db
from base.features.book.book_vo import Book
from base.features.user.user_vo import User


class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column('id', String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    remark = db.Column('remark', String(255), nullable=False)
    quantity = db.Column('quantity', Integer, nullable=False)
    price = db.Column('price', Float, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    book_id = db.Column('book_id', String(36),
                        ForeignKey(Book.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    user_id = db.Column('user_id', String(36),
                        ForeignKey(User.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __init__(self):
        db.create_all()


@event.listens_for(Expense, 'after_insert')
@event.listens_for(Expense, 'after_update')
@event.listens_for(Expense, 'after_delete')
def update_book_updated_at(mapper, connection, target):
    try:
        # Get the foreign key value of the related book
        book_id = target.book_id
        # Query the Book record based on the foreign key value
        book = Book.query.get(book_id)
        # Update the updated_at column of the Book
        book.updated_at = datetime.utcnow()
        # Set the committed value of the updated_at attribute
        # set_committed_value(book, 'updated_at', book.updated_at)
        db.session.add(book)  # Add the book object to the session
        db.session.flush()  # Flush changes to the database
        print("Book updated successfully.")
    except Exception as e:
        # Handle exceptions gracefully
        print("Error updating book:", e)

