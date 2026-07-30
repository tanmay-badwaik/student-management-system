from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.student import Student

student_bp = Blueprint("student", __name__, url_prefix="/students")

@student_bp.route("/")
def students():
    return render_template("students.html")

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

        return redirect(url_for("student.add_student"))

    return render_template("add_student.html")