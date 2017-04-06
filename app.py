from flask import Flask
import os

app=Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
env =os.environ['APP_SETTINGS']
app.config.from_object(env)
# app.config.from_envvar(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])



@app.route('/')
def hello():
	return "hello world"


@app.route('/<name>')
def hello1(name):
	return "Hello {} !".format(name)

if __name__=="__main__":
	app.run()