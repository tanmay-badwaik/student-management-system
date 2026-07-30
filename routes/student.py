from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.student import Student

student_bp = Blueprint("student", __name__, url_prefix="/students")

@student_bp.route("/")
def students():

    students = Student.query.all()

    return render_template(
        "students.html",
        students=students
    )

@student_bp.route("/edit_student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.name = request.form["name"]
        student.email = request.form["email"]
        student.course = request.form["course"]

        db.session.commit()

        return redirect(url_for("student.students"))

    return render_template(
        "edit_student.html",
        student=student
    )
    
@student_bp.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        student = Student(
            name=name,
            email=email,
            course=course
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("student.students"))

    return render_template("add_student.html")