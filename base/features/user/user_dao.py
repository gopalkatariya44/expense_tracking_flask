import datetime

import jwt

from base import settings, db
from base.features.user.user_vo import User


class UserDAO:

    @staticmethod
    def get_user(user_vo: User) -> User:
        user = User.query.filter(User.email == user_vo.email, User.password == user_vo.password).all()
        if user:
            return user[0]
        else:
            return None

    @staticmethod
    def create_user(user_vo):
        db.session.add(user_vo)
        db.session.commit()

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                settings.JWT_SECRET_KEY,
                algorithm='HS256'

            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, settings.JWT_SECRET_KEY, algorithms="HS256")
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
