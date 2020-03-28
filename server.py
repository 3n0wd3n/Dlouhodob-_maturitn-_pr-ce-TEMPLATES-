from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/accesbara')
def accesbara():
	return render_template('accesbara.html')

@app.route('/baraspage')
def baraspage():
	return render_template('baraspage.html')

app.run("127.0.0.1", 4444, debug=True)
