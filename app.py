from flask import Flask,render_template

app = Flask(__name__)


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


if __name__ == "__main__":
	app.run(debug=True)