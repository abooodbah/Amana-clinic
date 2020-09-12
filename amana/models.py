from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from amana import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_ar = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content_ar = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=False)


class NewsPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_ar = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    content_ar = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=False)



class Service(db.Model):
    __tablename__ = 'service'
    __mapper_args__ = {'polymorphic_identity': 'service'}
    id = db.Column(db.Integer, primary_key=True)
    title_ar = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=False)
    title_Font_size = db.Column(db.Integer, nullable=False, default=18)
    content_ar = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=False)
    content_Font_size = db.Column(db.Integer, nullable=False, default=12)
    subservices = db.relationship('SubService', backref='parent Service', lazy=True)
    service_type = db.Column(db.String(32), nullable=False, default=__tablename__)
    __mapper_args__ = {'polymorphic_on': service_type}

    def __repr__(self):
        return f"Service('{self.title_ar}', '{self.title_en}')"



class MainService(Service):
    __tablename__= 'main_service'
    id = db.Column(db.Integer, db.ForeignKey('service.id'),primary_key=True)
    service_type = db.Column(db.String(32), nullable=False, default=__tablename__)
    __mapper_args__ = {
        'polymorphic_identity':'main_service'
    }

class HemorrhiodsService(Service):
    __tablename__ = 'hemorrhiods_service'
    id = db.Column(db.Integer, db.ForeignKey('service.id'),primary_key=True)
    service_type = db.Column(db.String(32), nullable=False, default=__tablename__)
    __mapper_args__ = {
        'polymorphic_identity':'hemorrhiods_service'
    }

class SubService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_ar = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=False)
    title_Font_size = db.Column(db.Integer, nullable=False, default=18)
    content_ar = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=False)
    content_Font_size = db.Column(db.Integer, nullable=False, default=12)
    Service = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)
    def __repr__(self):
        return f"Service('{self.title_ar}', '{self.title_en}')"



class Information_and_Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Main_page_intro_title_ar = db.Column(db.Text, nullable=False)
    Main_page_intro_title_en = db.Column(db.Text, nullable=False)
    Main_page_intro_details_ar = db.Column(db.Text, nullable=False)
    Main_page_intro_details_en = db.Column(db.Text, nullable=False)
    Introduction_ar = db.Column(db.Text, nullable=False)
    Introduction_en = db.Column(db.Text, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"intro('{self.title_ar}', '{self.date_posted}')"


class Appointment(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service = db.Column(db.String(60), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)