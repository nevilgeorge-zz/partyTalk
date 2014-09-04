import os
PWD = os.path.abspath(os.curdir)

DEBUG=True
SQLALCHEMY_DATABASE_URI = 'postgres://kevcnomntfzocq:HGUhWi6Pwig7ApH7lWjyMThBEE@ec2-54-163-249-168.compute-1.amazonaws.com:5432/d8vanlqphigt0r'
#SQLALCHEMY_DATABASE_URI = 'postgres://PhilipHouse:house@localhost/party'
SECRET_KEY = 'thisissecret'
CSRF_ENABLED = True
SESSION_PROTECTION = 'strong'
