from flask import Blueprint, render_template

student_bp = Blueprint("student", __name__)


@student_bp.route("/students")
def students():
    return render_template("students.html")


@student_bp.route("/add-student")
def add_student():
    return render_template("add_student.html")  