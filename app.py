import os
import logging
from functools import wraps
from flask import Flask, request, jsonify, session
from src.main import register_user, login_user, logout_user, create_task, delete_task, hash_password, sanitize_input

app = Flask(__name__)

# LOGGING: Basic request and error logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# SECURITY: Load secret key from environment variables (never hardcode)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['JSON_SORT_KEYS'] = False

users_db = {}
tasks_db = []


# LOGGING: Log every incoming request
@app.before_request
def log_request():
    logger.info("REQUEST - %s %s - IP: %s", request.method, request.path, request.remote_addr)


# LOGGING: Log every outgoing response
@app.after_request
def log_response(response):
    logger.info("RESPONSE - %s %s - Status: %s", request.method, request.path, response.status_code)
    return response


# SECURITY: Authentication middleware to protect sensitive routes
def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            logger.warning("UNAUTHORIZED - %s %s - No active session", request.method, request.path)
            return jsonify({"success": False, "message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return jsonify({"message": "USTP Nexus API is running.", "version": "v1.0"})


@app.route("/register", methods=["POST"])
def register():
    # SECURITY: Input validation - sanitize all inputs
    if not request.is_json:
        logger.warning("REGISTER - Bad request: non-JSON content type")
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400

    data = request.get_json()
    email = sanitize_input(data.get("email", ""), max_length=254)
    password = data.get("password", "")

    if not email or not password:
        logger.warning("REGISTER - Bad request: missing email or password")
        return jsonify({"success": False, "message": "Invalid request format."}), 400

    result = register_user(email, password, list(users_db.keys()))
    if result["success"]:
        users_db[email] = hash_password(password)
        logger.info("REGISTER - Success: %s", email)
    else:
        logger.warning("REGISTER - Failed for %s: %s", email, result.get("message"))

    return jsonify(result), 200 if result["success"] else 400


@app.route("/login", methods=["POST"])
def login():
    # SECURITY: Input validation
    if not request.is_json:
        logger.warning("LOGIN - Bad request: non-JSON content type")
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400

    data = request.get_json()
    email = sanitize_input(data.get("email", ""), max_length=254)
    password = data.get("password", "")

    if not email or not password:
        logger.warning("LOGIN - Bad request: missing email or password")
        return jsonify({"success": False, "message": "Invalid request format."}), 400

    result = login_user(email, password, users_db)
    if result["success"]:
        session["user"] = email
        logger.info("LOGIN - Success: %s", email)
    else:
        logger.warning("LOGIN - Failed for %s", email)

    return jsonify(result), 200 if result["success"] else 401


@app.route("/logout", methods=["POST"])
@require_login
def logout():
    user = session.get("user")
    result = logout_user(session)
    logger.info("LOGOUT - %s", user)
    return jsonify(result), 200


@app.route("/tasks", methods=["GET"])
@require_login
def get_tasks():
    logger.info("GET TASKS - User: %s", session.get("user"))
    return jsonify({"tasks": tasks_db}), 200


@app.route("/tasks", methods=["POST"])
@require_login
def add_task():
    # SECURITY: Input validation
    if not request.is_json:
        logger.warning("ADD TASK - Bad request: non-JSON content type")
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 400

    data = request.get_json()
    title = sanitize_input(data.get("title", ""), max_length=200)
    due_date = sanitize_input(data.get("due_date", ""), max_length=100)

    result = create_task(title, due_date, tasks_db)
    if result["success"]:
        logger.info("ADD TASK - Success: '%s' by %s", title, session.get("user"))
    else:
        logger.warning("ADD TASK - Failed: %s", result.get("message"))

    return jsonify(result), 200 if result["success"] else 400


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@require_login
def remove_task(task_id):
    result = delete_task(task_id, tasks_db)
    if result["success"]:
        logger.info("DELETE TASK - ID %s deleted by %s", task_id, session.get("user"))
    else:
        logger.warning("DELETE TASK - ID %s not found", task_id)

    return jsonify(result), 200 if result["success"] else 404


# SECURITY: Error handlers to prevent information disclosure
@app.errorhandler(404)
def not_found(e):
    logger.warning("404 - Endpoint not found: %s %s", request.method, request.path)
    return jsonify({"success": False, "message": "Endpoint not found."}), 404


@app.errorhandler(500)
def server_error(e):
    logger.error("500 - Internal server error: %s %s - %s", request.method, request.path, str(e))
    return jsonify({"success": False, "message": "Internal server error."}), 500


if __name__ == "__main__":
    app.run(debug=False)
