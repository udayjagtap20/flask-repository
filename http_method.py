from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_students():
    data = request.get_json()
    new_student = {"id": len(students) + 1, "name": data["name"]
    }
    students.append(new_student)

    return {"message": "Student added sucessfully"},201
if __name__ =="__main__":
    app.run(debug=True)
