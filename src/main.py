import re
import hashlib
 
 
def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))
 
 
def validate_password(password: str) -> bool:
    """Returns True if password is at least 8 characters."""
    return isinstance(password, str) and len(password) >= 8
 
 
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
 
 
 
def register_user(email: str, password: str, existing_emails: list) -> dict:
    if not validate_email(email):
        return {"success": False, "message": "Invalid email format."}
    if not validate_password(password):
        return {"success": False, "message": "Password must be at least 8 characters."}
    if email in existing_emails:
        return {"success": False, "message": "Email already registered."}
    return {"success": True, "message": "Registration successful."}
 
 
def login_user(email: str, password: str, users_db: dict) -> dict:
    if email not in users_db:
        return {"success": False, "message": "Invalid credentials."}
    if users_db[email] != hash_password(password):
        return {"success": False, "message": "Invalid credentials."}
    return {"success": True, "message": "Login successful."}
 
 
def logout_user(session: dict) -> dict:
    session.clear()
    return {"success": True, "message": "Logged out successfully."}
 

def create_task(title: str, due_date: str, task_list: list) -> dict:
    if not title or not title.strip():
        return {"success": False, "message": "Task title cannot be empty."}
    if not due_date or not due_date.strip():
        return {"success": False, "message": "Due date cannot be empty."}
    task = {"id": len(task_list) + 1, "title": title.strip(), "due_date": due_date.strip()}
    task_list.append(task)
    return {"success": True, "message": "Task created.", "task": task}
 
 
def delete_task(task_id: int, task_list: list) -> dict:
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            return {"success": True, "message": "Task deleted."}
    return {"success": False, "message": "Task not found."}
