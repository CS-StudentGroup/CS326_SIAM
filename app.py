import os
from functools import wraps
from flask import Flask, request, jsonify, session
from src.main import register_user, login_user, logout_user, create_task, delete_task, hash_password, sanitize_input

app = Flask(__name__)

# SECURITY: Load secret key from environment variables (never hardcode)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['JSON_SORT_KEYS'] = False

users_db = {}
tasks_db = []


# SECURITY: Authentication middleware to protect sensitive routes
def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return jsonify({"success": False, "message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return jsonify({"message": "USTP Nexus API is running.", "version": "v0.8"})


@app.route("/register", methods=["POST"])
def register():
    # SECURITY: Input validation - sanitize all inputs
    if not request.is_json:
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    email = sanitize_input(data.get("email", ""), max_length=254)
    password = data.get("password", "")
    
    # SECURITY: Don't expose details about what failed in registration
    if not email or not password:
        return jsonify({"success": False, "message": "Invalid request format."}), 400

    result = register_user(email, password, list(users_db.keys()))
    if result["success"]:
        users_db[email] = hash_password(password)

    return jsonify(result), 200 if result["success"] else 400


@app.route("/login", methods=["POST"])
def login():
    # SECURITY: Input validation
    if not request.is_json:
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    email = sanitize_input(data.get("email", ""), max_length=254)
    password = data.get("password", "")
    
    if not email or not password:
        return jsonify({"success": False, "message": "Invalid request format."}), 400

    result = login_user(email, password, users_db)
    if result["success"]:
        session["user"] = email

    return jsonify(result), 200 if result["success"] else 401


@app.route("/logout", methods=["POST"])
@require_login
def logout():
    result = logout_user(session)
    return jsonify(result), 200


@app.route("/tasks", methods=["GET"])
@require_login
def get_tasks():
    # SECURITY: Only return tasks for authenticated user (future enhancement)
    return jsonify({"tasks": tasks_db}), 200


@app.route("/tasks", methods=["POST"])
@require_login
def add_task():
    # SECURITY: Input validation
    if not request.is_json:
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    title = sanitize_input(data.get("title", ""), max_length=200)
    due_date = sanitize_input(data.get("due_date", ""), max_length=100)

    result = create_task(title, due_date, tasks_db)
    return jsonify(result), 200 if result["success"] else 400


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@require_login
def remove_task(task_id):
    result = delete_task(task_id, tasks_db)
    return jsonify(result), 200 if result["success"] else 404


# SECURITY: Error handlers to prevent information disclosure
@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "message": "Endpoint not found."}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "message": "Internal server error."}), 500



if __name__ == "__main__":
    app.run(debug=False)
