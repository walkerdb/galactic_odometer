from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import date
from relativespeedsite.forms import DateForm, SingleFieldDateForm
from relativespeedsite.functions import calculate_facts
import chronyk

app = Flask(__name__)
app.config.update(WTF_CSRF_ENABLED=True,
                  SECRET_KEY="lol",
                  DEBUG=True)


@app.route('/', methods=['GET', 'POST'])
def index():
	form = SingleFieldDateForm()
	if request.method == "POST" and not form.birth_date.errors:
		try:
			print(form.birth_date)
			birthdate = chronyk.Chronyk(form.birth_date.data, allowfuture=False)
		except chronyk.DateRangeError:
			flash("Greetings, time-traveler... Maybe try something more realistic this time.")
			return render_template("index.html", form=form)
		except ValueError:
			flash("Sorry, I couldn't parse that. Try rephrasing?")
			return render_template("index.html", form=form)

		birthdate = date.fromtimestamp(birthdate.timestamp())
		facts = calculate_facts(birthdate)
		print(facts)
		return render_template("index.html", facts=facts, form=form)
	elif form.birth_date.errors:
		flash(form.birth_date.errors[0])
		return render_template("index.html", form=form)
	else:
		print("I failed")
		return render_template("index.html", form=form)


if __name__ == '__main__':
	app.run()
