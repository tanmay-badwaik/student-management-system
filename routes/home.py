from flask import Blueprint, render_template

from models.student import Student
from models.user import User

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():

    total_students = Student.query.count()

    total_users = User.query.count()

    return render_template(
        "index.html",
        total_students=total_students,
        total_users=total_users
    )