from flask import Flask, render_template
from os import environ
import functools

app=Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return render_template('hello.html', my_name=name)

@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname, lastname):

    return render_template('jedi.html', jedi= lastname[:3] + firstname[:2])
    
if __name__ == "__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))
    


