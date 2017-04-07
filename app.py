from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)

env =os.environ['APP_SETTINGS']
app.config.from_object(env)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)


@app.route('/')
def hello():
	return "hello world"


@app.route('/<name>')
def hello1(name):
	return "Hello {} !".format(name)

if __name__=="__main__":
	app.run()