
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from amana.models import User, Service
from amana import add_style_if_ar
from flask_babel import lazy_gettext as _
from datetime import datetime

class ContactForm(FlaskForm):
    name = StringField(_('name'),
                        validators=[DataRequired(), Email()])
    email = StringField(_('Email'),
                        validators=[DataRequired(), Email()])
    subject = StringField(_('Subject'),
                        validators=[DataRequired(), Email()])
    message = TextAreaField(_('Message'),
                        validators=[DataRequired(), Email()])
    image =  FileField(_('upload the file'), validators=[DataRequired(),FileAllowed(['jpg', 'png', 'svg'])])
    submit = SubmitField(_('Send Message'))

class BookingForm(FlaskForm):
    service = SelectField(_('Choose a medical service'), choices=[])
    name = StringField(_('name'),
                        validators=[DataRequired(), Email()])
    phone = StringField(_('phone'),
                        validators=[DataRequired(), Email()])
    email = StringField(_('Email'),
                        validators=[DataRequired(), Email()])
    date =  DateField(_('Date'),
                        validators=[DataRequired()], default=datetime.date(datetime.now()))
    message = TextAreaField(_('Message'),
                        validators=[DataRequired(), Email()])
    submit = SubmitField(_('Send Message'))


def generate_services(locale):
    services = list()
    for service in Service.query.all():
        add(services,value =  service.title_en if locale == 'en' else (service.title_ar),key = service.title_en if locale == 'en' else (service.title_ar))
    add(services, value = _('consultation'), key = _('consultation'))
    print(len(services))
    return services



def add(list, value, key):
    choice = (key,value)
    list.append(choice)