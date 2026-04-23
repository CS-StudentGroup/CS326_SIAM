import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from main import register_user, add_pad, delete_pad, get_pad

def test_register_valid_user():
    result = register_user("landlord@rentals.com", "securepass123", [])
    assert result["success"] is True

# BUG-001: Intentional failure for the defect log (Off-by-one error in main.py)
def test_register_exactly_8_char_password():
    result = register_user("landlord@rentals.com", "pass1234", []) 
    assert result["success"] is True, f"BUG-001: {result['message']}"

def test_add_pad_valid():
    pad_list = []
    result = add_pad("Room A", 5000.00, pad_list)
    assert result["success"] is True
    assert len(pad_list) == 1
    assert pad_list[0]["room_name"] == "Room A"

def test_add_pad_negative_price():
    result = add_pad("Room B", -500.00, [])
    assert result["success"] is False

def test_add_pad_empty_name():
    result = add_pad("", 5000.00, [])
    assert result["success"] is False

def test_delete_existing_pad():
    pad_list = [{"id": 1, "room_name": "Room A", "monthly_price": 5000.00, "is_occupied": False}]
    result = delete_pad(1, pad_list)
    assert result["success"] is True
    assert len(pad_list) == 0

def test_get_existing_pad():
    pad_list = [{"id": 1, "room_name": "Room A", "monthly_price": 5000.00, "is_occupied": False}]
    result = get_pad(1, pad_list)
    assert result["success"] is True
    assert result["pad"]["room_name"] == "Room A"