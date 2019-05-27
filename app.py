
import os
import sys, os
sys.path.append("/src")
from model import model

print(os.getcwd())

from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route("/handle_data/", methods=['POST', 'GET'])
def f_data():
    title = request.form.get('title')
    author = request. \
        form.get('author')
    date = request.form.get('date')
    section = request.form.get('section')
    if title and author and date and section is not None:
        try:
            saver(title, author, date, section)
            return
        except:
            print("database error")
    else:
        print("error")

    return

if __name__ == '__main__':
    app.run()
import contrler
