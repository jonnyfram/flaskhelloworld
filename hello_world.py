from flask import Flask
from os import environ
import functools

app=Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname, lastname):
    html = """
    <h1>
        {}{}
    """
    return html.format(lastname[:3],firstname[:2])
    
if __name__ == "__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))
    


