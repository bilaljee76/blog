from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Hello Flask!</h1>"

@app.route("/about")
def about_page():
    return "<h1>About page</h1>"

@app.route("/contact")
def contact_page():
    return "<h1>Contact page</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"

# @app.route("/student/<id>")
# def student(id):
#     return f"Student ID is {id}"

# "Is Bilal an ID?"

# "No."

# Exactly. We need to tell Flask Only numbers are allowed. This is called a Converter.

@app.route("/student/<int:id>")
def student(id):
    return f"Student ID is {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price is Rs. {amount}"

# @app.route("/files/<path:filename>")
# def files(filename):
#     return f"Requested File: {filename}"

if __name__ == "__main__":
    app.run(debug=True)