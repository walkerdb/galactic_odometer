from flask.ext.wtf import Form
from wtforms import validators, IntegerField
from datetime import date

class DateForm(Form):
	birth_day = IntegerField("Day of birth", validators=[
		validators.DataRequired(message="Birth day is required"),
		validators.NumberRange(min=1, max=31, message="Invalid day")])
	birth_month = IntegerField("Month of birth", validators=[
		validators.DataRequired(message="Birth month is required"),
		validators.NumberRange(min=1, max=12, message="Invalid month")])
	birth_year = IntegerField("Year of birth", validators=[
		validators.DataRequired(message="Birth year is required"),
		validators.NumberRange(min=0, max=date.today().year, message="Invalid year")])
