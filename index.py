from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    p = [
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"},
        {'t': 'wip', 'url': "https://github.com/mitchkarns/website", 'title': "Another test for wip projs"},
        {'t': 'wip', 'url': "https://github.com/mitchkarns/website", 'title': "Another test for wip projs"}
    ]
    return render_template('projects.html', p=p)

if __name__ == '__main__':
    app.run()