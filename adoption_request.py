from utils import generate_request_id, get_current_time


class AdoptionRequest:
    """
    Represents an adoption request for a shelter cat.
    """
    def __init__(self, person_name, phone, email, cat, message):
        self.person_name = person_name
        self.phone = phone
        self.email = email
        self.cat = cat
        self.message = message

        self.request_id = generate_request_id()
        self.status = "new"
        self.created_at = get_current_time()

    def show_info(self):
        print(f"Request ID: {self.request_id}")
        print(f"Person: {self.person_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Cat: {self.cat.name}")
        print(f"Message: {self.message}")
        print(f"Status: {self.status}")
        print(f"Date: {self.created_at}")


    def mark_contacted(self):
        if self.status != "new":
            return False

        self.status = "contacted"
        return True

    def approve(self):
        if self.status not in ["new", "contacted"]:
            return False

        if not self.cat.is_available():
            return False

        if not self.cat.reserve():
            return False

        self.status = "approved"
        return True

    def reject(self):
        if self.status in ["new", "contacted"]:
            self.status = "rejected"
            return True
        else:
            return False
