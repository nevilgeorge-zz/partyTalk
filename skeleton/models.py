from datetime import datetime
import os
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship, synonym, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" Post """
class Post(Base):
	__tablename__ = 'post'

	id = Column(Integer, primary_key=True)
	text = Column(Text)

	def __init__(self, text):
		self.text = text

""" Vote """ 
class Vote(Base):
	__tablename__ = 'vote'

	id = Column(Integer, primary_key=True)
	post_id = Column(Integer)
	value = Column(Integer)

	def __init__(self, post_id, value):
		self.post_id = post_id
		self.value = value

if __name__ == '__main__':
	#from datetime import timedelta

	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker

	#PWD = os.path.abspath(os.curdir)

	engine = create_engine('postgres://kevcnomntfzocq:HGUhWi6Pwig7ApH7lWjyMThBEE@ec2-54-163-249-168.compute-1.amazonaws.com:5432/d8vanlqphigt0r', echo=True)

	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	user = Post(text="It's too warm in here!")
	session.add(user)
	session.commit()

	vote = Vote(post_id=user.id, value=1)
	session.add(vote)
	session.commit()
