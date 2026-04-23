from flask import Flask, request, jsonify, session
from src.main import register_user, login_user, logout_user, create_task, delete_task, hash_password

app = Flask(__name__)
app.secret_key = "ustp-nexus-secret"

users_db = {}
tasks_db = []


@app.route("/")
def index():
    return jsonify({"message": "USTP Nexus API is running.", "version": "v0.5"})



@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    result = register_user(email, password, list(users_db.keys()))
    if result["success"]:
        users_db[email] = hash_password(password)

    return jsonify(result), 200 if result["success"] else 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    result = login_user(email, password, users_db)
    if result["success"]:
        session["user"] = email

    return jsonify(result), 200 if result["success"] else 401


@app.route("/logout", methods=["POST"])
def logout():
    result = logout_user(session)
    return jsonify(result), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks_db}), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title", "")
    due_date = data.get("due_date", "")

    result = create_task(title, due_date, tasks_db)
    return jsonify(result), 200 if result["success"] else 400


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    result = delete_task(task_id, tasks_db)
    return jsonify(result), 200 if result["success"] else 404



if __name__ == "__main__":
    app.run(debug=False)
