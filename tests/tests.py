import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from main import hash_password, register_user, login_user, logout_user, create_task, delete_task, hash_password



def test_register_valid_user():
    result = register_user("student@ustp.edu.ph", "securepass123", [])
    assert result["success"] is True

def test_register_duplicate_email():
    result = register_user("student@ustp.edu.ph", "securepass123", ["student@ustp.edu.ph"])
    assert result["success"] is False
    assert "already registered" in result["message"]

def test_register_invalid_email():
    result = register_user("not-an-email", "securepass123", [])
    assert result["success"] is False

def test_register_short_password():
    result = register_user("student@ustp.edu.ph", "123", [])
    assert result["success"] is False

# BUG-001: validate_password uses > 8 instead of >= 8
# This test FAILS on the buggy code, PASSES after the fix
def test_register_exactly_8_char_password():
    result = register_user("student@ustp.edu.ph", "pass1234", [])  # exactly 8 chars
    assert result["success"] is True, f"BUG-001: {result['message']}"



def test_login_valid_credentials():
    db = {"student@ustp.edu.ph": hash_password("securepass123")}
    result = login_user("student@ustp.edu.ph", "securepass123", db)
    assert result["success"] is True

def test_login_wrong_password():
    db = {"student@ustp.edu.ph": hash_password("securepass123")}
    result = login_user("student@ustp.edu.ph", "wrongpassword", db)
    assert result["success"] is False

def test_login_unregistered_email():
    result = login_user("ghost@ustp.edu.ph", "securepass123", {})
    assert result["success"] is False



def test_logout_clears_session():
    session = {"user_id": 1, "email": "student@ustp.edu.ph"}
    result = logout_user(session)
    assert result["success"] is True
    assert len(session) == 0



def test_create_task_valid():
    task_list = []
    result = create_task("Submit Lab Report", "2025-05-01", task_list)
    assert result["success"] is True
    assert len(task_list) == 1

def test_create_task_empty_title():
    result = create_task("", "2025-05-01", [])
    assert result["success"] is False

def test_create_task_no_due_date():
    result = create_task("Submit Lab Report", "", [])
    assert result["success"] is False



def test_delete_existing_task():
    task_list = [{"id": 1, "title": "Submit Lab Report", "due_date": "2025-05-01"}]
    result = delete_task(1, task_list)
    assert result["success"] is True
    assert len(task_list) == 0

def test_delete_nonexistent_task():
    result = delete_task(99, [])
    assert result["success"] is False
