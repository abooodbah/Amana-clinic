from flask import render_template, request, Blueprint
from amana.models import FAQ,NewsPost,MainService,HemorrhiodsService,Information_and_Records
from amana.posts.forms import ServiceForm
from amana import mail
from amana.models import User
from amana import app, bcrypt, mail
from sqlalchemy import event
from werkzeug.security import generate_password_hash


main = Blueprint('main', __name__)


@app.context_processor
def inject_user():
    mainServices = MainService.query.all()
    hemorrhiodsServices = HemorrhiodsService.query.all()
    info = Information_and_Records.query.first()
    return dict(info=info, mainServices=mainServices, hemorrhiodsServices=hemorrhiodsServices)

@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
	if value != oldvalue:
		return bcrypt.generate_password_hash(value).decode('utf-8')
	return value

@event.listens_for(MainService.service_type, 'set', retval=True)
def setType(target, value, oldvalue, initiator):
	return 'main_service'

@event.listens_for(HemorrhiodsService.service_type, 'set', retval=True)
def setType(target, value, oldvalue, initiator):
	return 'hemorrhiods_service'

@main.route("/contact")
def contact():
    form = contactform()
    return render_template('contact.html')

@main.route("/")
@main.route("/home")
def home():
    news = NewsPost.query.all()
    FAQs = FAQ.query
    info = Information_and_Records.query.first()
    Services = MainService.query.all()
    return render_template('mainxx.html', news = news[-3:], FAQs = FAQs, Services = Services, posts =True, slider= True,info = info)


@main.route("/about")
def about():
    info = Information_and_Records.query.first()
    FAQs = FAQ.query
    return render_template('about.html', title='About', info = info, FAQ= FAQs)


@main.route("/Services")
def services():
    servicetype = request.args.get('type')
    info = Information_and_Records.query.first()
    if ('main' in servicetype):
        Services = MainService.query.all()
    else:
        Services = HemorrhiodsService.query.all()
    return render_template('Service.html', title='MainService', legend='New MainService', Services = Services,info = info)

@main.route("/news")
def news():
    info = Information_and_Records.query.first()
    Services = MainService.query.all()
    return render_template('MainService.html', title='MainService', legend='New MainService', Services = Services,info = info)
