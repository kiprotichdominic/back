from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "efec7e52ccb4a3e86ec302b43fce90fa1c167ba1"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ratings.db"
db = SQLAlchemy(app)
login_manager= LoginManager(app)
bcrypt = Bcrypt(app)

# import blueprints
from app.main.views import main
from app.users.views import users
from app.ratings.views import ratings

#register bluepprints
app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(ratings)
