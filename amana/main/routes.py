from flask import render_template, request, Blueprint, flash, redirect, url_for, current_app
from amana.models import FAQ,NewsPost,MainService,HemorrhiodsService,Information_and_Records,Service
from amana.models import User
from amana import app, bcrypt, mail, get_locale
from amana.main.forms import ContactForm,BookingForm, generate_services
from sqlalchemy import event
from werkzeug.security import generate_password_hash
from PIL import Image
from flask_mail import Message
import os
from datetime import datetime 
from flask_babel import lazy_gettext as _


main = Blueprint('main', __name__)


@app.context_processor
def inject():
    mainServices = MainService.query.all()
    hemorrhiodsServices = HemorrhiodsService.query.all()
    info = Information_and_Records.query.first()
    date = datetime.date(datetime.now())
    return dict(info=info, mainServices=mainServices, hemorrhiodsServices=hemorrhiodsServices, date = date)


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


@main.route("/contact", methods=['GET', 'POST'])
def contact():
    contactform = ContactForm()
    bookingform = BookingForm()
    bookingform.service.choices = generate_services(get_locale())
    print()
    if contactform.email.data and contactform.name.data and not bookingform.phone.data:
        msg = Message(contactform.subject.data,
                  sender='Amanaclinicemail@gmail.com',
                  recipients=[contactform.email.data])
        msg.body = f'''from: {contactform.email.data}
Sender: {contactform.name.data}

{contactform.message.data}
                '''
        msg.attach("image.png", "image/png", contactform.image.data.read())  
        mail.send(msg)
        flash(_('Your message has been sent'), 'success')
        return redirect(url_for('main.contact'))

    if bookingform.email.data and bookingform.phone.data:
        msg = Message('Appointment on {bookingform.date.data}',
                  sender='Amanaclinicemail@gmail.com',
                  recipients=[bookingform.email.data])
        msg.body = f'''from: {bookingform.email.data}
Sender: {bookingform.name.data}
Phone: {bookingform.phone.data}
Service: {bookingform.service.data}
{bookingform.message.data}
                '''
        mail.send(msg)
        flash(_('Your appointment has been booked'), 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html', contactform = contactform, bookingform = bookingform)

@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def home():
    FAQs = FAQ.query
    info = Information_and_Records.query.first()
    Services = Service.query.all()[-9:]
    contactform = ContactForm()
    bookingform = BookingForm()
    bookingform.service.choices = generate_services(get_locale())
    print()
    if contactform.email.data and contactform.name.data and not bookingform.phone.data:
        msg = Message(contactform.subject.data,
                  sender='Amanaclinicemail@gmail.com',
                  recipients=['Amanaclinic1@gmail.com',contactform.email.data])
        msg.body = f'''from: {contactform.email.data}
Sender: {contactform.name.data}

{contactform.message.data}
                '''
        msg.attach("image.png", "image/png", contactform.image.data.read())  
        mail.send(msg)
        flash(_('Your message has been sent'), 'success')
        return redirect(url_for('main.contact'))

    if bookingform.email.data and bookingform.phone.data:
        msg = Message('Appointment on {bookingform.date.data}',
                  sender='Amanaclinicemail@gmail.com',
                  recipients=['Amanaclinic1@gmail.com',bookingform.email.data])
        msg.body = f'''from: {bookingform.email.data}
Sender: {bookingform.name.data}
Phone: {bookingform.phone.data}
Service: {bookingform.service.data}
{bookingform.message.data}
                '''
        mail.send(msg)
        flash(_('Your appointment has been booked'), 'success')
        return redirect(url_for('main.contact'))
    return render_template('mainxx.html', Services = Services, slider= True,info = info, contactform=contactform, bookingform=bookingform)


@main.route("/about")
def about():
    info = Information_and_Records.query.first()
    FAQs = FAQ.query
    return render_template('about.html', title='About', info = info, FAQ= FAQs)


@main.route("/Services", methods=['GET', 'POST'])
def services():
    servicetype = request.args.get('type')
    info = Information_and_Records.query.first()
    if ('main' in servicetype):
        Services = MainService.query.all()
    else:
        Services = HemorrhiodsService.query.all()

    contactform = ContactForm()
    bookingform = BookingForm()
    bookingform.service.choices = generate_services(get_locale())
    print()
    if contactform.email.data and contactform.name.data and not bookingform.phone.data:
        msg = Message(contactform.subject.data,
                  sender='Amanaclinicemail@gmail.com',
                  recipients=[contactform.email.data])
        msg.body = f'''from: {contactform.email.data}
Sender: {contactform.name.data}

{contactform.message.data}
                '''
        msg.attach("image.png", "image/png", contactform.image.data.read())  
        mail.send(msg)
        flash(_('Your message has been sent'), 'success')
        return redirect(url_for('main.contact'))

    if bookingform.email.data and bookingform.phone.data:
        msg = Message('Appointment on {bookingform.date.data}',
                  sender='Amanaclinicemail@gmail.com',
                  recipients=[bookingform.email.data])
        msg.body = f'''from: {bookingform.email.data}
Sender: {bookingform.name.data}
Phone: {bookingform.phone.data}
Service: {bookingform.service.data}
{bookingform.message.data}
                '''
        mail.send(msg)
        flash(_('Your appointment has been booked'), 'success')
        return redirect(url_for('main.contact'))
    return render_template('Service.html', title='MainService', legend='New MainService', Services = Services,info = info, contactform=contactform, bookingform=bookingform)

@main.route("/news")
def news():
    info = Information_and_Records.query.first()
    Services = MainService.query.all()
    return render_template('MainService.html', title='MainService', legend='New MainService', Services = Services,info = info)



