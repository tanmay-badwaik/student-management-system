# from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
from models import db
from models.student import Student
from sqlalchemy import or_

student_bp = Blueprint("student", __name__, url_prefix="/students")

@student_bp.route("/")
def students():
    if "user_id" not in session:

        flash(
            "Please login first!",
            "warning"
        )

        return redirect(
            url_for("auth.login")
        )
    
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    
    query = Student.query

    if search:

        students = Student.query.filter(

        or_(

            Student.name.ilike(f"%{search}%"),
            Student.email.ilike(f"%{search}%"),
            Student.course.ilike(f"%{search}%")

        )

    )
    students = query.paginate(
        page=page,
        per_page=5
    )

    return render_template(
        "students.html",
        students=students,
        search=search
    )

@student_bp.route("/edit_student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.name = request.form["name"]
        student.email = request.form["email"]
        student.course = request.form["course"]

        db.session.commit()
        flash("Student updated successfully!", "success")


        return redirect(url_for("student.students"))

    return render_template(
        "edit_student.html",
        student=student
    )
    
    
@student_bp.route("/delete/<int:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully!", "success")
    return redirect(url_for("student.students"))


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
        
        flash("Student added successfully!", "success")

        return redirect(url_for("student.students"))

    return render_template("add_student.html")