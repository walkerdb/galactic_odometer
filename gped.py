from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import date
from relativespeedsite.forms import DateForm
from relativespeedsite.functions import calculate_facts

app = Flask(__name__)
app.config.update(WTF_CSRF_ENABLED = True,
                  SECRET_KEY = "lol",
                  DEBUG = True)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = DateForm()
	error = None
	print(form.errors)
	if form.validate_on_submit():

		try:
			birthdate = date(int(form.birth_year.data), int(form.birth_month.data), int(form.birth_day.data))
		except:
			flash("Date not valid (probably too many days in your month) - try something else")
			return render_template("index.html", form=form)
		if birthdate > date.today():
			flash("Your date is in the future!")
			return render_template("index.html", form=form)

		facts = calculate_facts(birthdate)
		return render_template('index.html', facts=facts, form=form)

	elif request.method == "POST":
		flash("Please enter numerical values only")
		errors = [form.birth_day.errors, form.birth_month.errors, form.birth_year.errors]
		for error in errors:
			if error:
				flash(error[0])
		return render_template('index.html', form=form)

	else:
		return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run()
