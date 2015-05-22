from flask.ext.wtf import Form
from wtforms import validators, StringField

class DateForm(Form):
	valid_items = [validators.DataRequired()]
	birth_day = StringField("Day of birth", validators=valid_items.append(validators.NumberRange(
		min=1, max=31, message="Invalid day")))
	birth_month = StringField("Month of birth", validators=valid_items.append(validators.NumberRange(
		min=1, max=12, message="Invalid month")))
	birth_year = StringField("Year of birth", validators=valid_items.append(validators.NumberRange(
		min=0, max=2014, message="Invalid year")))
