#!/usr/bin/env python

import datetime
import simplejson
from flask import Flask, render_template
from jinja2 import Markup


class Config(object):
	DEBUG = True


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
	timestamp = datetime.datetime.utcnow()
	timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%S Z")
	return render_template("index.html", timestamp=Markup(simplejson.dumps(timestamp)))


if __name__ == '__main__':
	app.run()
