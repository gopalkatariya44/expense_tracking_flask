from datetime import datetime

import pytz
from sqlalchemy import func
from sqlalchemy.orm import aliased

from base import db
from base.features.book.book_vo import Book
from base.features.expense.expense_vo import Expense


class BookDAO:
    @staticmethod
    def get_book(id):
        book = Book.query.filter_by(id=id).all()
        return book[0]

    @staticmethod
    def create_book(book_vo):
        db.session.add(book_vo)
        db.session.commit()

    @staticmethod
    def update_book(book_vo):
        db.session.merge(book_vo)
        db.session.commit()

    @staticmethod
    def delete_book(id):
        book = BookDAO.get_book(id)
        db.session.delete(book)
        db.session.commit()

    @staticmethod
    def book_list(user_id):
        book_list = db.session.query(
            Book.id,
            Book.name,
            func.date_format(
                func.convert_tz(Book.updated_at, '+00:00', '+05:30'),
                "%d %b, %Y %I:%i %p"
            ).label('local_updated_at'),
            func.sum(func.coalesce(Expense.price * Expense.quantity, 0)).label('total_expense')
        ).outerjoin(Expense, (Book.id == Expense.book_id) & (Expense.user_id == user_id)) \
            .group_by(Book.id, Book.name) \
            .order_by(Book.updated_at.desc()) \
            .all()
        return book_list

    @staticmethod
    def local_to_utc(date, time):
        local_datetime = datetime.strptime(date+" "+time, "%Y-%m-%d %H:%M")
        local_tz = pytz.timezone('Asia/Kolkata')
        localized_datetime = local_tz.localize(local_datetime)
        utc_datetime = localized_datetime.astimezone(pytz.utc)
        return utc_datetime
