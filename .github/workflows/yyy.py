from flask import Flask, render_template_string, redirect, request, url_for
register_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>register website</title>
</head>
<body>
<h1>register page Welcome to register</h1>
{% if message %}
	<p>{{message}}</p>
{% endif %}
<form method="post">
Username: <input type="text" name="username">
Password: <input type="password" name="password">
<button>register</button>
<a href ="{{url_for('login')}}">already have account login now</a>
</form>
</body>
</html>
"""
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>login page</title>
</head>
<body>
<h1>login page</h1>
{% if message %}
	<p>{{message}}</p>
{% endif %}
<form method="post">
Username: <input type="text" name="username" required>
Password: <input type="password" name="password" required>
<button>login</button>
<a href="{{url_for('register')}}">create account for login</a>
"""
home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>home page</title>
</head>
<body> 
{% if message %}
	<p>{{message}}</p>
{% endif %}
<h1>welcome to home </h1>
<a href="{{url_for('login')}}">logout</a>
</body>
</html>
"""
app = Flask(__name__)
users = {}
@app.route("/home")
def home():
	return render_template_string(home_page, message="")
@app.route("/register", methods=["GET", "POST"])
def register():
	message = ""
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if username in users:
			message = "username is already exists please choose another username"
		elif not username or  not password:
			message = "the field has to be fill before proceed"
		elif len(password) < 8:
			message = "password must be atleast 8 character"
		else:
			users[username] = password
			message = "account created succefully"
			return render_template_string(login_page, message=message)
	return render_template_string(register_page, message=message)
@app.route("/login", methods=["GET", "POST"])
def login():
	message =""
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if username in users and users[username] == password:
			message = "account login succefully\n welcome "
			return render_template_string(home_page, message=message)
		else:
			message = "invalid username or password"
			return render_template_string(login_page, message=message)
	return render_template_string(login_page, message=message)	
if __name__ == "__main__":
	app.run(debug=True)