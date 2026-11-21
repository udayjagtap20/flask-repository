
from flask import Flask, request, jsonify

app = Flask(__name__)

students = {
    1: {"name": "Uday", "course": "BSc IT"},
    2: {"name": "Priya", "course": "BSc IT"},
    3: {"name": "Rahul", "course": "BCA"}
}


@app.route("/")
def home():
    return "Welcome to Flask Practice!"


@app.route("/students")
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>")
def get_student(student_id):
    student = students.get(student_id)

    if student:
        return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.route("/students/search")
def search_student():
    name = request.args.get("name")

    for student in students.values():
        if student["name"].lower() == name.lower():
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
