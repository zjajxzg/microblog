from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Bill'}
    #return 'hello,world!'
    posts = [{'author':{'nickname':'john'},
              'body':'beautiful day in hangzhou'},
             {'author': {'nickname': 'susan'},
              'body': 'not a good day'}
             ]
    return render_template('index.html',title = 'Home',user = user,posts = posts)