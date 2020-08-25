from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128), nullable=False)
    translations = relationship('Translation', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Translation(db.Model):
    __tablename__ = 'translation'

    id = Column(Integer, primary_key=True)
    lang_from = Column(String(16))
    lang_detected = Column(String(16))
    lang_to = Column(String(16))
    text_from = Column(Text)
    text_to = Column(Text)
    time = Column(DateTime(timezone=True), default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Translation {self.text_from}>'
