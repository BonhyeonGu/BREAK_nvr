from flask import redirect, url_for, render_template
from view import app

@app.route("/")
def root():
	return redirect(url_for('index'))

@app.route("/index")
def index():
	return render_template('live.html')

@app.route("/live")
def live():
	return render_template('live.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)