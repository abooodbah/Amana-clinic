from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, BooleanField
from wtforms.fields.html5 import DateTimeLocalField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class FAQForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class NewsBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


class TimingForm(FlaskForm):
    FromDay = StringField('Title', validators=[DataRequired()])
    ToDAY = TextAreaField('Content', validators=[DataRequired()])
    startTime = TextAreaField('Content', validators=[DataRequired()])
    EndTime = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class BookAppointmentForm(FlaskForm):
    date = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y', validators=[DataRequired()])

