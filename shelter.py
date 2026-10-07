class Shelter:
    """
    Represents a cat shelter.
    """
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

        self.cats = []
        self.requests = []
        self.donations = []

    def add_cat(self, cat):
        self.cats.append(cat)
        return True

    def find_cat_by_id(self, cat_id):
        for cat in self.cats:
            if cat.cat_id == cat_id:
                return cat
        return None

    def find_cat_by_name(self, name):
        for cat in self.cats:
            if cat.name == name:
                return cat
        return None

    def show_all_cats(self):
        for cat in self.cats:
            cat.show_info()

    def show_available_cats(self):
        for cat in self.cats:
            if cat.is_available():
                cat.show_info()

    def add_adoption_request(self, request):
        if not request.cat.is_available():
            return False
        self.requests.append(request)
        return True

    def add_donation(self, donation):
        if donation.is_valid():
            self.donations.append(donation)
            return True
        return False

    def show_donations(self):
        for donation in self.donations:
            donation.show_info()
