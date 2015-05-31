from flask.ext.wtf import Form
from wtforms import validators, IntegerField, StringField
from datetime import date

class SingleFieldDateForm(Form):
	birth_date = StringField("Birthdate", validators=[
		validators.DataRequired(message="You need to enter your birthdate!")
	])