from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFormStudent

app = Flask(__name__)

app.config["SECRET_KEY"] = "d2c3113ee16531331a94a16f82b0cd1e"


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


@app.route("/student_register", methods=["GET", "POST"])
def student_register():
    form = RegistrationFormStudent()
    if form.validate_on_submit():

        flash(f"Object created for {form.name.data}!", "success")
        return redirect(url_for("students"))
    return render_template("register.html", title="Student Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
