from flask import Flask, redirect, url_for, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import inspect

app = Flask(__name__)
app.config.from_object(Config)

### DB configuration ###
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import models

##################
### Blueprints ###
##################
from app.blueprints.home import bp as home_bp
from app.blueprints.dashboard import bp as dashboard_bp

app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')


#############
### Admin ###
#############
class MyModelView(ModelView):
    # can_delete = False

    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargss):
        return redirect('/')



admin = Admin(app)


