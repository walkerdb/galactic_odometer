from flask.ext.wtf import Form
from wtforms import validators, StringField

class SingleFieldDateForm(Form):
    birth_date = StringField("Birthdate", validators=[
        validators.DataRequired(message="You need to enter your birthdate!")
    ])