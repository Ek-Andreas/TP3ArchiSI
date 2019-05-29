import os
import sys

sys.path.append("/src")
from model.model import saver

print(os.getcwd())

from flask import *

app = Flask(__name__, template_folder='view')


@app.route("/handle_data/", methods=['POST', 'GET'])
def f_data():
    title = request.form.get('title')
    author = request.form.get('author')
    date = request.form.get('date')
    section = request.form.get('section')
    if title and author and date and section is not None:
        saver(title, author, date, section)
    else:
        return render_template('add_book.html')
    return home_query()


if __name__ == '__main__':
    app.run()


def home_query():
    import view.templateHome
    from mako.template import Template
    from model.model import cursor
    cursor.execute("SELECT DISTINCT title, author, date, section FROM books")
    rows = [list(i) for i in cursor.fetchall()]
    template = view.templateHome.get_template()
    html = (Template(template).render(rows=rows))
    return html


@app.route('/')
def main():
    return home_query()


@app.route('/addBooks')
def add():
    return render_template('add_book.html')


@app.route("/searchBooks/", methods=['POST', 'GET'])
def search():
    value = request.form.get('value')
    return search(value)


def search(value):
    import view.templateSearch
    from mako.template import Template
    from model.model import cursor
    query = "SELECT DISTINCT title, author, date, section FROM books WHERE title = '" + value +"'"
    print(query)
    cursor.execute(query)
    rows = [list(i) for i in cursor.fetchall()]
    template = view.templateSearch.get_template()
    html = (Template(template).render(rows=rows))
    return html
