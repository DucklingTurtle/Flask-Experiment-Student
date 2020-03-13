from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationFormStudent, RegistrationFormTeacher

app = Flask(__name__)
app.config["SECRET_KEY"] = "d2c3113ee16531331a94a16f82b0cd1e"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

# database models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    focus1 = db.Column(db.String(30), nullable=False)
    focus2 = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)

    def __repr__(self):
        return f"Student('{self.name}', '{self.focus1}', '{self.focus2}', '{self.email}')"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    focus1 = db.Column(db.String(30), nullable=False)
    focus2 = db.Column(db.String(30), nullable=False)
    days_avail = db.Column(db.String(40), nullable=False)
    hours = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    students = db.Column(db.String(40))
    day1 = db.Column(db.String(40))
    day2 = db.Column(db.String(40))
    day3 = db.Column(db.String(40))
    day4 = db.Column(db.String(40))
    day5 = db.Column(db.String(40))
    day6 = db.Column(db.String(40))
    day7 = db.Column(db.String(40))
    day8 = db.Column(db.String(40))
    day9 = db.Column(db.String(40))
    day10 = db.Column(db.String(40))
    hours_taken = db.Column(db.String(40))
    first_pass = db.Column(db.String(40))


# create students in database
def create_student(name, focus1, focus2, email):
    student = Student(name=name, focus1=focus1, focus2=focus2, email=email)
    db.session.add(student)
    db.session.commit()

# create teachers in database
def create_teacher(name, focus1, focus2, days_avail, hours, email):
    teacher = Teacher(name=name, focus1=focus1, focus2=focus2, days_avail=days_avail, hours=hours, email=email)
    db.session.add(teacher)
    db.session.commit()


# get list of students
def get_students_list():
    students_list = Student.query.all()
    return students_list

# get list of teachers
def get_teachers_list():
    teachers_list = Teacher.query.all()
    return teachers_list


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

@app.route("/admin_students")
def admin_students():
    students_list = get_students_list()
    return render_template("admin_students.html", students_list=students_list)

@app.route("/admin_teachers")
def admin_teachers():
    teachers_list = get_teachers_list()
    return render_template("admin_teachers.html", teachers_list=teachers_list)

@app.route("/student_register", methods=["GET", "POST"])
def student_register():
    form = RegistrationFormStudent()
    if form.validate_on_submit():
        name = form.name.data
        focus1 = form.focus1.data
        focus2 = form.focus2.data
        email = form.email.data
        create_student(name, focus1, focus2, email)
        flash(f"Database entry created for {form.name.data}!", "success")
        return redirect(url_for("students"))
    return render_template("register.html", title="Student Register", form=form)


@app.route("/teacher_register", methods=["GET", "POST"])
def teacher_register():
    form = RegistrationFormTeacher()
    if form.validate_on_submit():
        if request.method == "POST":
            name = form.name.data
            focus1 = form.focus1.data
            focus2 = form.focus2.data
            days = str(request.form.getlist("days_checkbox"))
            hours = str(request.form.getlist("hours_checkbox"))
            email = form.email.data
            create_teacher(name, focus1, focus2, days, hours, email)
            flash(f"Database entry created for {form.name.data}!", "success")
            return redirect(url_for("teachers"))
    return render_template("register_t.html", title="Teacher Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
