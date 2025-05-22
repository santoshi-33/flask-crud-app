from flask import Flask ,render_template # Capital F

app = Flask(__name__)    # Capital F again

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",title="Evaluate",number="num")




#start the app
if __name__ == "__main__":  # Add spaces around __name__ and ==, and fix 'if'
    app.run(debug=True)


