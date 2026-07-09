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

@app.route("/contact")
def contact():

	return render_template(

	"contact.html",

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
    


if __name__ == "__main__":
	app.run(debug=True)