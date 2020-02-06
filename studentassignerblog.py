import gspread, sys, Student_Register_Sheet
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFormStudent
from oauth2client.service_account import ServiceAccountCredentials

# google sheets
# s_r = Student_Register_Sheet.worksheet
s_r = Student_Register_Sheet.client.open("Student_Register_Database").sheet1

app = Flask(__name__)

app.config["SECRET_KEY"] = "d2c3113ee16531331a94a16f82b0cd1e"

def create_student(student_id, name, focus1, focus2, email):
    len_sheet = len(s_r.col_values(1))
    cell = len_sheet + 1
    s_r.update_cell(cell, 1, student_id)
    s_r.update_cell(cell, 2, name)
    s_r.update_cell(cell, 3, focus1)
    s_r.update_cell(cell, 4, focus2)
    s_r.update_cell(cell, 5, email)

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
    # print(len_sheet, file=sys.stderr)
    if form.validate_on_submit():
        student_id = form.student_id.data
        name = form.name.data
        focus1 = form.focus1.data
        focus2 = form.focus2.data
        email = form.email.data
        create_student(student_id, name, focus1, focus2, email)
        # len_sheet = len(s_r.col_values(1))
        # cell = len_sheet + 1
        # s_r.update_cell(cell, 1, form.student_id.data)
        # s_r.update_cell(cell, 2, form.name.data)
        # s_r.update_cell(cell, 3, form.focus1.data)
        # s_r.update_cell(cell, 4, form.focus2.data)
        # s_r.update_cell(cell, 5, form.email.data)
        flash(f"Database entry created for {form.name.data}!", "success")
        return redirect(url_for("students"))
    return render_template("register.html", title="Student Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
