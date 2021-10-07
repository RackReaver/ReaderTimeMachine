from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageName='Dashboard')

@app.route('/search', methods=['POST'])
def search():
    params = request.form['search-field']
    r = requests.get('https://www.googleapis.com/books/v1/volumes?q="' + params + '"')
    data = r.json()
    return render_template('search.html', search=data, pageName='Search Results for "{}"'.format(params))



if __name__ == ("__main__"):
    app.run(debug=False)
