from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from amana.config import Config
from flask_babel import Babel

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

#import Environment Varibales
app.config.from_object(Config)

#jinja2 additional controls 
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize Flask Sql Alchemy & Firebase Firestore
db = SQLAlchemy(app)

#Initialize Flask_Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Initialize Flask-Babel
babel = Babel(app)

# Initialize Flask-Mail
mail = Mail(app)

# Initialize Flask-Mail
manager = Manager(app)

# Initialize Flask-Mail
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#LanguageSelector()
@babel.localeselector
def get_locale():
	if request.args.get('locale'):
		return request.args.get('locale')
	else:	
		return 'ar'

#add get_locale() to jinja2 context
app.jinja_env.globals['get_locale'] = get_locale

#handles routing exception
def handle_routing_exception(value):
    try:
        return url_for('main.' + request.path.replace('/',''), locale = 'ar' if (value and 'ar' in value) else 'en')
    except:
        return url_for('users.' + request.path.replace('/',''), locale = 'ar' if (value and 'ar' in value) else 'en')

#add handle_routing_exception() to jinja2 context
app.jinja_env.globals['handle_routing_exception'] = handle_routing_exception

#handles specific style additions for arabic users
def add_style_if_ar(style: str, style_en = ''):
    if (get_locale() and ('ar' in get_locale())):
    	return str(style)
    else:
    	return style_en

#add add_style_if_ar() to jinja2 context
app.jinja_env.globals['add_style_if_ar'] = add_style_if_ar

#Register Blueprints
from amana.users.routes import users
app.register_blueprint(users)

from amana.posts.routes import posts
app.register_blueprint(posts)

from amana.main.routes import main
app.register_blueprint(main)

from amana.errors.handlers import errors
app.register_blueprint(errors)

#Initialize flask_admin
from amana.utils import secure_model_view, secure_index_view, setup_admin_account
setup_admin_account()
admin = Admin(app, index_view=secure_index_view())
#add views to flask_admin
from amana.models import User, FAQ, NewsPost, MainService, HemorrhiodsService, SubService,Service, Information_and_Records
admin.add_view(secure_model_view(Information_and_Records, db.session))
admin.add_view(secure_model_view(MainService, db.session))
admin.add_view(secure_model_view(HemorrhiodsService, db.session))
admin.add_view(secure_model_view(SubService, db.session))
admin.add_view(secure_model_view(FAQ, db.session))



