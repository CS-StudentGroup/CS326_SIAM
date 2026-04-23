import re
import hashlib

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

def get_pad(pad_id: int, pad_list: list) -> dict:
    """
    Retrieves a pad by its ID.

    Args:
        pad_id: The ID of the pad to retrieve.
        pad_list: The list of pads to search within.

    Returns:
        A dict with 'success' (bool), 'message' (str), and 'pad' (dict) if found.
    """
    for pad in pad_list:
        if pad["id"] == pad_id:
            return {"success": True, "message": "Pad found.", "pad": pad}
    return {"success": False, "message": "Pad not found."}