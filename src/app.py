from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

@app.route('/resenas')
def resenas():
    return render_template('resenas.html')

@app.route('/veganclub')
def veganclub():
    return render_template('veganclub.html')

    
if __name__ == '__main__':
    app.run(debug=True)