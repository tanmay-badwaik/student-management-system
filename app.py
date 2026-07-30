from flask import Flask

from config import Config
from models import db

from routes.home import home_bp
from routes.student import student_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(student_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# from flask import Flask,render_template

# app = Flask(__name__)


# @app.route("/")
# def home():
#     # return "<h1>Welcome to Student Management System</h1>"
#     # return "<h1>Hello Tanmay! 🚀</h1>"
#     return render_template("index.html")

# @app.route("/students")
# def students():
#     return render_template("students.html")


# @app.route("/add-student")
# def add_student():
#     return render_template("add_student.html")

# if __name__ == "__main__":
#     app.run(debug=True)