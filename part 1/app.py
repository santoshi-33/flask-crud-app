from flask import Flask  # Capital F

app = Flask(__name__)    # Capital F again

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the home page</h1>"

@app.rout("/about")
def about():
    return "<h1>Welcome to the about page</h1>"

@app.route("/welcome/<name>")
def welcome(home):
    return f"<h1>{name},Welcome to this page</h1>"

@app.route("/addition/<int:num1>/<int:num2")
def addition(num1,num2):
    return f"<h1>imput is{num1}+{num2},output is {num +10}</h1>"

if __name__ == "__main__":  # Add spaces around __name__ and ==, and fix 'if'
    app.run(debug=True)


