from utils import generate_donation_id, get_current_time


class Donation:
    """
    Represents a donation to the shelter or a specific cat.
    """

    def __init__(self, donor_name, purpose, amount, cat):
        self.donation_id = generate_donation_id()
        self.donor_name = donor_name
        self.purpose = purpose
        self.amount = amount
        self.cat = cat
        self.created_at = get_current_time()

    def is_valid(self):
        if self.amount > 0:
            return True
        elif self.amount <= 0:
            return False

    def show_info(self):
        print(f"Donation ID: {self.donation_id}")
        print(f"Donor Name: {self.donor_name}")
        print(f"Amount: {self.amount}")
        print(f"Purpose: {self.purpose}")

        if self.cat is None:
            print("For: General shelter support")

        else:
            print(f"For cat: {self.cat.name}")

        print(f"Date: {self.created_at}")
