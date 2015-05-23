from flask import render_template, request
from datetime import date
from relativespeedsite.forms import DateForm
from relativespeedsite.functions import calculate_facts
from relativespeedsite import app


@app.route('/', methods=['GET', 'POST'])
def index():
	form = DateForm()
	if request.method == 'POST' and form.validate():
		birthdate = date(int(form.birth_year.data), int(form.birth_month.data), int(form.birth_day.data))
		facts = calculate_facts(birthdate)
		print("No, me!")
		return render_template('index.html', facts=facts, form=form)
	elif request.method == "POST" and not form.validate():
		pass
	else:
		print("me!")
		return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run()
