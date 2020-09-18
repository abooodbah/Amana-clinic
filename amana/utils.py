from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from amana.models import User
from flask_login import current_user
from flask import abort
from amana import db
from flask import render_template, url_for, flash, redirect, request, Blueprint



class secure_model_view(ModelView):
	def is_accessible(self):
		print("Sucess-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('users.login'))



class secure_index_view(AdminIndexView):
	def is_accessible(self):
		print("Sucess-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('users.login'))

def is_admin(user: User):
	return False
	admin = User.query.first()
	if user == admin:
		return True
	return False


def setup_admin_account():
	if not User.query.filter_by(username = 'admin').first() :
		user = User(username='admin', email='amana_clinic1@hotmail.com', password='t3t3t3t3')
		db.session.add(user)
		db.session.commit()
	user = User.query.filter_by(username = 'admin').first()