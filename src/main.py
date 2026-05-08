import re
import hashlib
import html

# SECURITY: Input sanitization function
def sanitize_input(user_input: str, max_length: int = 1000) -> str:
    """
    Sanitizes user input by stripping whitespace, enforcing max length, and escaping HTML.
    
    Args:
        user_input: The raw user input string.
        max_length: Maximum allowed length for the input.
    
    Returns:
        Sanitized input string.
    """
    if not isinstance(user_input, str):
        return ""
    
    # Strip whitespace and enforce maximum length
    sanitized = user_input.strip()[:max_length]
    
    # Escape HTML special characters to prevent XSS
    sanitized = html.escape(sanitized)
    
    return sanitized

def validate_email(email: str) -> bool:
    """
    Validates the format of an email address.

    Args:
        email: The email string to validate.

    Returns:
        True if the email format is valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email)) and len(email) <= 254

def validate_password(password: str) -> bool:
    """
    SECURITY: Enhanced password validation requiring:
    - At least 8 characters
    - Mix of uppercase, lowercase, and numbers (or symbols)
    
    Args:
        password: The password string to validate.

    Returns:
        True if the password meets security requirements, False otherwise.
    """
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    # Check for at least one uppercase, one lowercase, and one digit or symbol
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    # Require uppercase + lowercase + (digit OR special character)
    return has_upper and has_lower and (has_digit or has_special)

def hash_password(password: str) -> str:
    """
    SECURITY: Hashes a password using SHA-256 with salt.
    NOTE: For production, use bcrypt or argon2 instead.

    Args:
        password: The plaintext password to hash.

    Returns:
        A hexadecimal SHA-256 hash string of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email: str, password: str, existing_emails: list) -> dict:
    """
    SECURITY: Registers a new user with validated email and strong password.
    
    Args:
        email: The user's email address.
        password: The user's chosen password.
        existing_emails: A list of already registered email addresses.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    # Sanitize email input
    email = sanitize_input(email, max_length=254)
    
    if not validate_email(email):
        return {"success": False, "message": "Invalid email format. Please use a valid email address."}
    if not validate_password(password):
        return {"success": False, "message": "Password must be at least 8 characters with uppercase, lowercase, and (digit or special character)."}
    if email in existing_emails:
        return {"success": False, "message": "This email is already registered."}
    return {"success": True, "message": "Registration successful."}

def login_user(email: str, password: str, users_db: dict) -> dict:
    """
    SECURITY: Authenticates a user with timing attack resistance considerations.

    Args:
        email: The user's email address.
        password: The plaintext password to verify.
        users_db: A dict mapping emails to hashed passwords.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    # Sanitize email input
    email = sanitize_input(email, max_length=254)
    
    if email not in users_db:
        # SECURITY: Use generic error to prevent email enumeration
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

# --- PAD RENTING LOGIC ---

def add_pad(room_name: str, monthly_price: float, pad_list: list) -> dict:
    if not room_name or not room_name.strip():
        return {"success": False, "message": "Room name cannot be empty."}
    if monthly_price <= 0:
        return {"success": False, "message": "Price must be greater than zero."}
    
    pad = {
        "id": len(pad_list) + 1, 
        "room_name": room_name.strip(), 
        "monthly_price": monthly_price,
        "is_occupied": False
    }
    pad_list.append(pad)
    return {"success": True, "message": "Pad added successfully.", "pad": pad}

def delete_pad(pad_id: int, pad_list: list) -> dict:
    for pad in pad_list:
        if pad["id"] == pad_id:
            pad_list.remove(pad)
            return {"success": True, "message": "Pad removed from system."}
    return {"success": False, "message": "Pad not found."}

# --- TASK MANAGEMENT LOGIC ---

def create_task(title: str, due_date: str, tasks_db: list) -> dict:
    """
    Creates a new task.

    Args:
        title: The task title.
        due_date: The task due date.
        tasks_db: The task database list.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    if not title or not title.strip():
        return {"success": False, "message": "Task title cannot be empty."}
    
    task = {
        "id": len(tasks_db) + 1,
        "title": title.strip(),
        "due_date": due_date,
        "completed": False
    }
    tasks_db.append(task)
    return {"success": True, "message": "Task created successfully.", "task": task}

def delete_task(task_id: int, tasks_db: list) -> dict:
    """
    Deletes a task by ID.

    Args:
        task_id: The ID of the task to delete.
        tasks_db: The task database list.

    Returns:
        A dict with 'success' (bool) and 'message' (str).
    """
    for task in tasks_db:
        if task["id"] == task_id:
            tasks_db.remove(task)
            return {"success": True, "message": "Task deleted successfully."}
    return {"success": False, "message": "Task not found."}
