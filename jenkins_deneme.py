import os
from flask import Flask, request, g

print("jenkins api deneme başlıyor...")





app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World"

if __name__ == '__main__':
    app.run()


