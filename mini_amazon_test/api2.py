from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return 'welcome'

@app.route('/login',methods=['POST'])
def login():

	user={'username':'mk', 'password':'mikhi'}

	username = request.form['username']
	password = request.form['password']

	if user['username']==username:
		if user['password']==password:
			return redirect(url_for('welcome') )
		return 'wrong password'
	return 'wrong username'

if __name__=='__main__':
	app.run(debug=True)