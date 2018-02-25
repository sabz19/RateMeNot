from flask import Flask,render_template
import config

app = Flask()
app.config.from_object()
#app.config.from_envvar('APP_SETTINGS')

@app.route('/')
def home():
	return render_template('search.html')