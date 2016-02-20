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
        {'t': 'wip', 'url': "https://github.com/mitchkarns/bnb", 'title': "Direct Action Everywhere - Inhouse"},
        {'t': 'fin', 'url': "https://github.com/squeekur/node-js-sever", 'title': "Android App Backend - WareComm"},
        {'t': 'fin', 'url': "https://github.com/bkmunar/WareComm", 'title': "Android App - WareComm"},
        {'t': 'fin', 'url': "https://github.com/mitchkarns/website", 'title': "This Website"}
    ]
    return render_template('projects.html', p=p)

if __name__ == '__main__':
    app.run()