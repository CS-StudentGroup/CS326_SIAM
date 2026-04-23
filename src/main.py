import re
import hashlib


# Email and Password Validation

def validate_email(email: str) -> bool:
    """
    Validates the format of an email address.

    Args:
        email: The email string to validate.

    Returns:
        True if the email format is valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password: str) -> bool:
    """
    Checks if a password meets the minimum length requirement.

    Args:
        password: The password string to validate.

    Returns:
        True if the password is a string of at least 8 characters, False otherwise.
    """
    return isinstance(password, str) and len(password) >= 8


def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    Args:
        password: The plaintext password to hash.

    Returns:
        A hexadecimal SHA-256 hash string of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


# Authentication Logic

def register_user(email: str, password: str, existing_emails: list) -> dict:
    """
    Registers a new user if the email and password are valid and the email is not taken.

    Args:
        email: The user's email address.
        password: The user's chosen password.
        existing_emails: A list of already registered email addresses.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    if not validate_email(email):
        return {"success": False, "message": "Invalid email format."}
    if not validate_password(password):
        return {"success": False, "message": "Password must be at least 8 characters."}
    if email in existing_emails:
        return {"success": False, "message": "Email already registered."}
    return {"success": True, "message": "Registration successful."}


def login_user(email: str, password: str, users_db: dict) -> dict:
    """
    Authenticates a user by checking their email and hashed password.

    Args:
        email: The user's email address.
        password: The plaintext password to verify.
        users_db: A dict mapping emails to hashed passwords.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    if email not in users_db:
        return {"success": False, "message": "Invalid credentials."}
    if users_db[email] != hash_password(password):
        return {"success": False, "message": "Invalid credentials."}
    return {"success": True, "message": "Login successful."}


def logout_user(session: dict) -> dict:
    """
    Clears the current user session.

    Args:
        session: The session dictionary to clear.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    session.clear()
    return {"success": True, "message": "Logged out successfully."}


# Tasks

def create_task(title: str, due_date: str, task_list: list) -> dict:
    """
    Creates a new task and appends it to the task list.

    Args:
        title: The title of the task.
        due_date: The due date of the task as a string.
        task_list: The list to append the new task to.

    Returns:
        A dict with 'success' (bool), 'message' (str), and 'task' (dict) on success.
    """
    if not title or not title.strip():
        return {"success": False, "message": "Task title cannot be empty."}
    if not due_date or not due_date.strip():
        return {"success": False, "message": "Due date cannot be empty."}
    task = {"id": len(task_list) + 1, "title": title.strip(), "due_date": due_date.strip()}
    task_list.append(task)
    return {"success": True, "message": "Task created.", "task": task}


def delete_task(task_id: int, task_list: list) -> dict:
    """
    Deletes a task by its ID from the task list.

    Args:
        task_id: The integer ID of the task to delete.
        task_list: The list of tasks to search through.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            return {"success": True, "message": "Task deleted."}
    return {"success": False, "message": "Task not found."}
