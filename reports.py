def count_cats_by_status(cats):
    result = {"available": 0, "reserved": 0, "adopted": 0}
    for cat in cats:
        if cat.status in result:
            result[cat.status] += 1
    return result

def count_requests_by_status(requests):
    result= {"new": 0, "contacted": 0, "approved": 0, "rejected": 0}
    for request in requests:
        if request.status in result:
            result[request.status] += 1
    return result

def calculate_total_donations(donations):
    total = 0
    for donation in donations:
        total += donation.amount
    return total

def calculate_cat_donations(donations, cat):
    total = 0
    for donation in donations:
        if donation.cat == cat:
            total += donation.amount
    return total

def calculate_donations_by_purpose(donations, purpose):
    total = 0
    for donation in donations:
        if donation.purpose == purpose:
            total += donation.amount
    return total
