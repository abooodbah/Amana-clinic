from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from amana.models import User
from flask_login import current_user
from flask import abort


class secure_model_view(ModelView):
	def is_accessible(self):
		return is_admin(current_user)

	def inaccessible_callback(self, name, **kwargs):
		abort(403)
		return



class secure_index_view(AdminIndexView):
	def is_accessible(self):
		return is_admin(current_user)

def is_admin(user: User):
	return True
	admin = User.query.filter_by(username = 'admin').first()
	if user == admin:
		return True
	return False