from cat import Cat
from shelter import Shelter
from adoption_request import AdoptionRequest
from donation import Donation

import reports

shelter = Shelter("Happy Paws Shelter", "+46 70 123 45 67", "hello@happypaws.se")


mia = Cat(
    "Mia",
    2,
    "female",
    "Calm and affectionate cat. Loves people and quiet places.",
    "images/mia.jpg",
    True,
)

mike = Cat(
    "Mike",
    3,
    "male",
    "Loud and energetic cat. Loves to play and make noise.",
    "images/mike.jpg",
    True,
)

tom = Cat(
    "Tom",
    4,
    "male",
    "Independent and curious cat. Loves to explore and climb.",
    "images/tom.jpg",
    True,
)

bella = Cat(
    "Bella",
    1,
    "female",
    "Playful and friendly cat. Loves to cuddle and be petted.",
    "images/bella.jpg",
    True,
)

bob = Cat(
    "Bob",
    5,
    "male",
    "Friendly and loyal cat. Loves to play and explore.",
    "images/bob.jpg",
    True,
)


cats = [mia, mike, tom, bella, bob]

for cat in cats:
    shelter.add_cat(cat)


print("\n--- ALL CATS ---")
shelter.show_all_cats()


print("\n--- AVAILABLE CATS ---")
shelter.show_available_cats()


found_cat = shelter.find_cat_by_name("Mia")

if found_cat is not None:
    print("\nCat found:")
    found_cat.show_info()
else:
    print("Cat not found")


unknown_cat = shelter.find_cat_by_name("Bil")

if unknown_cat is None:
    print("\nBil was not found")


tom_id = tom.cat_id
found_by_id = shelter.find_cat_by_id(tom_id)

if found_by_id is not None:
    print("\nFound by ID:", found_by_id.name)


request1 = AdoptionRequest(
    "Anna", "+46 70 987 65 43", "anna@happypaws.se", mia, "I want to adopt Mia"
)

request2 = AdoptionRequest(
    "Frida", "+46 70 987 65 43", "frida@happypaws.se", mia, "I want to adopt Mia"
)


print("\nRequest 1 cat:", request1.cat.name)
print("Request 2 cat:", request2.cat.name)


request1_added = shelter.add_adoption_request(request1)
request2_added = shelter.add_adoption_request(request2)

print("\nRequest 1 added:", request1_added)
print("Request 2 added:", request2_added)
print("Requests:", len(shelter.requests))


print("\n--- ADOPTION REQUESTS ---")

request1.show_info()
request2.show_info()


request1_contacted = request1.mark_contacted()

print("\nRequest 1 contact result:", request1_contacted)
print("Request 1 status:", request1.status)


request2_contacted = request2.mark_contacted()

print("\nRequest 2 contact result:", request2_contacted)
print("Request 2 status:", request2.status)


request1_approved = request1.approve()
request2_approved = request2.approve()

print("\nRequest 1 approve:", request1_approved)
print("Request 1 status:", request1.status)

print("\nRequest 2 approve:", request2_approved)
print("Request 2 status:", request2.status)

print("\nMia status:", mia.status)


print("\n--- AVAILABLE CATS AFTER RESERVATION ---")

shelter.show_available_cats()


adopt_result = mia.adopt()

print("Adoption completed:", adopt_result)
print("Mia status:", mia.status)


request3 = AdoptionRequest(
    "Julia", "+46 70 444 55 66", "julia@email.com", mike, "I am interested in Mike."
)

shelter.add_adoption_request(request3)
request3.mark_contacted()
result_request3 = request3.reject()

print("Reject result:", result_request3)
print("Request status:", request3.status)
print("Mike status:", mike.status)


donation1 = Donation("Anna", "food", 500, mia)
donation2 = Donation("Max", "shelter", 1000, None)
donation3 = Donation("Julia", "medicine", 300, mike)
donation4 = Donation("Alex", "food", 600, None)
invalid_donation = Donation("Test", "food", -500, mia)


print(shelter.add_donation(donation1))
print(shelter.add_donation(donation2))
print(shelter.add_donation(donation3))
print(shelter.add_donation(donation4))
print(shelter.add_donation(invalid_donation))

print("Donations count:", len(shelter.donations))

print("\n--- DONATIONS ---")
shelter.show_donations()


cat_stats = reports.count_cats_by_status(shelter.cats)
print("\n--- CAT STATUS REPORT ---")

for status, count in cat_stats.items():
    print(f"{status}: {count}")

print("\n--- REQUEST STATUS REPORT ---")

request_stats = reports.count_requests_by_status(shelter.requests)
for status, count in request_stats.items():
    print(f"{status}: {count}")

print("\n--- DONATION REPORT ---")

total_donations = reports.calculate_total_donations(shelter.donations)
print("Total donations:", total_donations)


mia_donations = reports.calculate_cat_donations(shelter.donations, mia)
print("Total donations for Mia:", mia_donations)

food_donations = reports.calculate_donations_by_purpose(shelter.donations, "food")
print("Total donations for food:", food_donations)


print("\n--- DOCUMENTATION ---")

print(Cat.__doc__)
print(Shelter.__doc__)
print(Donation.__doc__)
print(AdoptionRequest.__doc__)

print("\n--- END ---")
