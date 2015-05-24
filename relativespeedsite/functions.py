from flask import Markup
from datetime import date
import humanize

def retrieve_miles_string(speed, total_days, description, class_="distance"):
	string = "You have traveled <span class='{2}'>{0}</span> miles {1}.\n".format(humanize.intword(total_days * speed * .62), description, class_)
	return string

def calculate_facts(birthdate):
	# speeds in km/h, taken from http://www.astrosociety.org/edu/publications/tnl/71/howfast.html
	earth_rot = 1600 * 24
	earth_orbit = 107000 * 24
	sun_orbit = 70000 * 24
	galaxy_rot = 792000 * 24
	galaxy_speed = 2100000 * 24
	cumulative = earth_rot + earth_orbit + sun_orbit + galaxy_rot + galaxy_speed

	date0 = birthdate
	date1 = date.today()
	date_delta = date1 - date0

	date_delta_days = date_delta.days

	facts = []
	facts.append(Markup(retrieve_miles_string(earth_rot, date_delta_days, "due to the rotation of the earth")))
	facts.append(Markup(retrieve_miles_string(earth_orbit, date_delta_days, "due to the orbit of the earth around the sun")))
	facts.append(Markup(retrieve_miles_string(sun_orbit, date_delta_days, "due to the the sun's relative motion through the galaxy")))
	facts.append(Markup(retrieve_miles_string(galaxy_rot, date_delta_days, "due to the rotation of the galaxy")))
	facts.append(Markup(retrieve_miles_string(galaxy_speed, date_delta_days, "from the motion of the Milky Way through the universe")))
	facts.append(Markup(retrieve_miles_string(cumulative, date_delta_days, "in your lifetime", class_="total_distance")))

	return facts

