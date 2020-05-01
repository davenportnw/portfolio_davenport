from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World!'


@app.route('/contact', methods=['GET','POST'])
def  contact():
    # Give me the information
    print(request.form['nombre'])
    print('nombre')
    return 'Contact ' + request.form['nombre']
   