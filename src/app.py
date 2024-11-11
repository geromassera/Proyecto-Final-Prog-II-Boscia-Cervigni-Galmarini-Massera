from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'veganclub'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
  
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder': 'Username'})
    email = StringField('Email', validators=[InputRequired()], render_kw={'placeholder': 'E-mail'})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ese nombre de usuario ya existe. Por favor, elija otro.')

    def validate_email(self, email):
        mail = User.query.filter_by(email=email.data).first()
        if mail:
            raise ValidationError('Ese correo electrónico ya está en uso. Por favor, elija otro.')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')

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

@app.route('/veganclub', methods=['GET', 'POST'])
def veganclub():
    register = RegisterForm()
    login = LoginForm()
    
    if register.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(register.password.data)
        new_user = User(username=register.username.data, email=register.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('veganclub.html', register=register, login=login)

    if login.validate_on_submit():
        user = User.query.filter_by(username=login.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, login.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
        
    return render_template('veganclub.html', register=register, login=login)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)