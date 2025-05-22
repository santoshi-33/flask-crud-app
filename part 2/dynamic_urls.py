from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page <h1>"

# @app.route("/welcome/steve")
# def welcome_steve():
#     return "<h1>HEY STEVE, WELCOME TO PAGE</h1>"

# @app.route("/welcome/tony")
# def welcome_tony():
#     return "<h1>HEY TONY, WELCOME TO PAGE</h1>"


#parameters 
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>HEY {name.title()}, WELCOME TO PAGE</h1>"


if __name__ == "__main__":
    app.run(debug=True)

