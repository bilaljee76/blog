from flask import Flask
from flask import render_template

from flask import request

from forms import ContactForm, LoginForm

# from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate, mail

from models import User,Role

import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

migrate.init_app(app, db)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "your_email@gmail.com"
app.config["MAIL_PASSWORD"] = "your_password"

mail.init_app(app)


app.config["SECRET_KEY"] = "my-secret-key"


@app.route("/")
def home_page():

	blog_name = "Flask Blog"

	owner = "Bilal Asghar"

	total_posts = 3

	posts= [

		"Introduction to Flask",

		"Understanding Routes",

		"Learning Jinja2"

		]

	return render_template(

		"index.html",

		blog_name = blog_name,

		owner = owner,

		total_posts = total_posts,

		posts = posts

		)


@app.route("/about")
def about_page():

	return render_template(

	"about.html",

	blog_name="Flask Blog"

    )


@app.errorhandler(404)
def page_not_found(error):

    return render_template(

        "404.html",

        blog_name="Flask Blog"

    ), 404

# @app.route("/error")
# def error():

# 	number=10/0

# 	return str(number)

@app.errorhandler(500)
def internal_server_error(error):

    return render_template(

        "500.html",

        blog_name="Flask Blog"

    ), 500


# @app.route("/contact", methods=["GET", "POST"])
# def contact_page():

#     if request.method == "POST":

#         name = request.form.get("name")
#         email = request.form.get("email")
#         phone = request.form.get("phone")
#         message = request.form.get("message")

#         print(name)
#         print(email)
#         print(phone)
#         print(message)

#     return render_template(
#         "contact.html",
#         blog_name="Flask Blog"
#     )

# For WTF
@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    form = ContactForm()

    if form.validate_on_submit():
        print(form.name.data)
        print(form.email.data)
        print(form.phone.data)
        print(form.message.data)

    return render_template(
        "contact.html",
        blog_name="Flask Blog",
        form=form
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        print("Username:", form.username.data)

        print("Password:", form.password.data)

        print("Remember Me:", form.remember_me.data)

    return render_template(
        "login.html",
        blog_name="Flask Blog",
        form=form
    )


# print(app.url_map)

if __name__ == "__main__":
	app.run(debug=True)