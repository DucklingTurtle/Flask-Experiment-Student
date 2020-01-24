from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/admin")
def admin():
    return render_template("administrator.html")


if __name__ == '__main__':
    app.run(debug=True)