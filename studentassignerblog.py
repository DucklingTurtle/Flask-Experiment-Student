import gspread, sys
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFormStudent
from oauth2client.service_account import ServiceAccountCredentials

# client google database
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('google-database.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Student_Register_Database").sheet1

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
    len_sheet = len(sheet.col_values(1))
    logger.debug(len_sheet, file=sys.stder)
    if form.validate_on_submit():
        len_sheet = len(sheet.col_values(1))
        print(len_sheet)
        flash(f"Object created for {form.name.data}!", "success")
        return redirect(url_for("students"))
    return render_template("register.html", title="Student Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
