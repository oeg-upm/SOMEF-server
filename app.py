import os
import json
from flask import Flask, render_template, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
#import requests
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        app.run(debug=True, port=int(sys.argv[1]))
    elif len(sys.argv) == 3 and sys.argv[2].isdigit():
        app.run(debug=True, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True)

