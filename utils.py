import random
from datetime import datetime

def get_current_time():
    """Returns the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_donation_id():
    """Generates a unique donation ID."""
    return f"DON-{random.randint(100000, 999999)}"


def generate_cat_id():
    """Generates a unique cat ID."""
    return f"CAT-{random.randint(1000, 9999)}"


def generate_request_id():
    """Generates a unique request ID."""
    return f"REQ-{random.randint(10000, 99999)}"
