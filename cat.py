from utils import generate_cat_id, get_current_time

class Cat:
    """
    Represents a cat in the shelter.
    """

    def __init__(self, name, age, gender,description, photo, sterilized):
        self.cat_id = generate_cat_id()
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description
        self.photo = photo
        self.sterilized = sterilized
        self.status = "available"
        self.created_at = get_current_time()

    def show_info(self):
        print(f"Cat ID: {self.cat_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Description: {self.description}")
        print(f"Photo: {self.photo}")
        print(f"Sterilized: {self.sterilized}")
        print(f"Status: {self.status}")
        print(f"Created at: {self.created_at}")

    def is_available(self):
        if self.status == "available":
            return True
        else:
            return False

    def reserve(self):
        if not self.is_available():
            return False
        self.status = "reserved"
        return True

    def adopt(self):
        if self.status != "reserved":
            return False
        self.status = "adopted" 
        return True

    def make_available(self):
        if self.status != "reserved":
            return False
        self.status = "available"
        return True
