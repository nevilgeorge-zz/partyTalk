from datetime import datetime
import os
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship, synonym, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" User """
class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	username = Column(String(200))
	password = Column(String(100))
	phone = Column(String(10))

	def __init__(self, name, password, phone):
		self.name = name
		self.password = password
		self.phone = phone

	def __repr__(self):
		return '<User %r>' % self.name

""" Aliases """
class Alias(Base):
	__tablename__ = 'alias'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship("User", backref('aliases', order_by=id))
	alias_name = Column(String(50))

	def __init__(self, user_id, alias):
		self.user_id = user_id
		self.alias_name = alias

	def __repr__(self):
		return '<Alias %r>' % self.alias_name

""" Reminders """ 
class Reminder(Base):
	__tablename__ = 'reminder'

	id = Column(Integer, primary_key=True)
	owner_id = Column(Integer, ForeignKey('user.id'))
	owner = relationship("Owner", backref('reminders', order_by=id))
	description = Column(String(200))

	def __init__(self, owner_id, description):
		self.owner_id = owner_id
		self.description = description

	def __repr__(self):
		return '<Reminder %r>' % self.description

if __name__ == '__main__':
	from datetime import timedelta

	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker

	PWD = os.path.abspath(os.curdir)

	engine = create_engine('sqlite:///reminder.db', echo=True)

	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()
