
import os
import sys, os
sys.path.append("/src")
from model import model

print(os.getcwd())

from flask import *

app = Flask(__name__)


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

def home_query():
    # f = open("templates/home.html", "w+")
    import templates.template
    from mako.template import Template
    from model.model import cursor
    cursor.execute("SELECT title, author, date, section FROM books")
    rows = [list(i) for i in cursor.fetchall()]
    template = templates.template.get_template()
    html = (Template(template).render(rows=rows))
    # f.close()
    return html
#home_query()



@app.route('/')
def main():
    return home_query()

@app.route('/addBooks')
def add():
    return render_template('add_book.html')