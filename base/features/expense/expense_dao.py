from datetime import datetime

import pytz
from sqlalchemy import func

from base import db
from base.features.expense.expense_vo import Expense


class ExpenseDAO:
    @staticmethod
    def get_expense(id):
        expense = Expense.query.filter_by(id=id).all()
        return expense[0]

    @staticmethod
    def create_expense(expense_vo):
        db.session.add(expense_vo)
        db.session.commit()

    @staticmethod
    def update_expense(expense_vo):
        db.session.merge(expense_vo)
        db.session.commit()

    @staticmethod
    def delete_expense(id):
        expense = ExpenseDAO.get_expense(id)
        db.session.delete(expense)
        db.session.commit()

    @staticmethod
    def expense_list(user_id):
        expense_list = db.session.query(
            Expense.id,
            Expense.remark,
            Expense.quantity,
            Expense.price,
            func.date_format(func.convert_tz(Expense.created_at, '+00:00', '+05:30'), "%d %b, %Y %I:%i %p").label(
                'local_created_at')
        ).filter_by(user_id=user_id).order_by(Expense.created_at.desc()).all()
        total = round(db.session.query(func.sum(Expense.quantity * Expense.price)).scalar(), 2)
        return expense_list, total

    @staticmethod
    def local_to_utc(date, time):
        local_datetime = datetime.strptime(date+" "+time, "%Y-%m-%d %H:%M")
        local_tz = pytz.timezone('Asia/Kolkata')
        localized_datetime = local_tz.localize(local_datetime)
        utc_datetime = localized_datetime.astimezone(pytz.utc)
        return utc_datetime
