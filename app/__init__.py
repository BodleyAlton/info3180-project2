from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
# from models import authenticate,identity
app = Flask(__name__)
app.config['SECRET_KEY'] = "super random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://altonbodley@127.0.0.1/proj2" # "postgresql://xwjtqjypnhqazc:dfc9c03e77be3aeb00a2863ef9dc5617308457fbacbeac6530ecaec70bade10c@ec2-50-19-95-47.compute-1.amazonaws.com:5432/db86ouco87v9g0"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= "./app/static/uploads"
app.config['ALLOWED_EXTENSIONS'] = "set(['png', 'jpg', 'jpeg', 'gif'])"

db = SQLAlchemy(app)

# jwt = JWT(app, models.authenticate, models.identity)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
