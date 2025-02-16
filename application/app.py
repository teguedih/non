from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    return render_template("index.html", name=name)

if _name_ == "_principal_":
    app.run(debug=True)
