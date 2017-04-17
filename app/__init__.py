from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "super random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://altonbodley@127.0.0.1/proj2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= "./app/static/uploads"
app.config['ALLOWED_EXTENSIONS'] = "set(['png', 'jpg', 'jpeg', 'gif'])"

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
