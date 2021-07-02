from flask import Flask, jsonify, render_template, request
import time
import random

app = Flask(__name__)

r = []
@app.route('/_stuff', methods = ['GET'])
def stuff():
    r.append(random.randint(0,100))
    return render_template('random.html', res = r)
    return jsonify(result = random.randint(0,10))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
