from flask import Flask, redirect, url_for, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from sqlalchemy import inspect

app = Flask(__name__)
app.config.from_object(Config)

### DB configuration ###
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


from app import models


@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))


##################
### Blueprints ###
##################
from app.blueprints.home import bp as home_bp
from app.blueprints.dashboard import bp as dashboard_bp
from app.blueprints.auth import bp as auth_bp

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
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

admin.add_view(MyModelView(models.User, db.session))
admin.add_view(MyModelView(models.Translation, db.session))

