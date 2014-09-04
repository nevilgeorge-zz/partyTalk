#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request, jsonify, make_response, Response, flash, redirect, session, url_for, g
from skeleton.models import Base,Post, Vote
from skeleton import config

from sqlalchemy import desc, and_
from sqlalchemy.orm import load_only
from operator import itemgetter

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
db.Model = Base

@app.route('/feed', methods = ['GET'])
def feed():
	posts = db.session.query(Post)
	post_tuple = []
	for post in posts:
		votes = db.session.query(Vote).filter_by(post_id=post.id)
		count = 0
		for vote in votes:
			count += vote.value
		post_tuple.append((post, count))

	post_tuple = sorted(post_tuple,key=itemgetter(1),reverse=True)
	return render_template('feed.html', posts=post_tuple)

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

@app.route('/post', methods = ['GET'])
def post():
	return render_template('post.html')

@app.route('/post_post', methods = ['POST'])
def postpost():
	text = request.form['text']
	new_post = Post(text)
	db.session.add(new_post)
	db.session.commit()
	return jsonify(result="success")

@app.route('/upvote/<post_id>', methods = ['GET'])
def upvote(post_id):
	new_vote = Vote(post_id, 1)
	db.session.add(new_vote)
	db.session.commit()
	return redirect(url_for('feed'))

@app.route('/downvote/<post_id>', methods = ['GET'])
def downvote(post_id):
	new_vote = Vote(post_id, -1)
	db.session.add(new_vote)
	db.session.commit()
	return redirect(url_for('feed'))

@app.route('/reload_feed', methods = ['GET'])
def reload():
	posts = db.session.query(Post)
	post_tuple = []
	for post in posts:
		votes = db.session.query(Vote).filter_by(post_id=post.id)
		count = 0
		for vote in votes:
			count += vote.value
		post_tuple.append((post, count))
	post_tuple = sorted(post_tuple,key=itemgetter(1),reverse=True)
	return render_template("element.html", posts=post_tuple)


