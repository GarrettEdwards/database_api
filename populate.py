import csv
import random
from rest_api.models import *

last_name = csv.reader(open('lastname.csv', 'r'))
female_file = csv.reader(open('female.csv', 'rb'))
male_file = csv.reader(open('male.csv', 'rb'))
event_info = csv.reader(open('event_info.csv', 'rb'))
vendors = csv.reader(open('Vendors.csv', 'rb'))
positions = csv.reader(open('Positions.csv', 'rb'))

def card_type():
    rand = random.randint(2)

    if rand == 0:
        return "mastercard"
    elif rand == 1:
        return "visa"
    else:
        return "american express"


def create_payment():
    p = Payment.objects.get_or_create()
    p.amount = "15"
    rand = random.randint(2)
    if rand == 0:
        p.type = 'cash'
        cash = Cash.objects.get_or_create()
        cash.payment_number = p.payment_number
        cash.save()
    elif rand == 1:
        p.type = 'card'
        card = Card.objects.get_or_create()
        card.payment_number = p.payment_number
        card.zipcode = str(random.randint(99999))
        card.card_number = str(random.randint(999999999999))
        card.card_type = card_type()
        card.save()
    else:
        p.type = 'check'
        p.check_number = random.randint(10000)
        check = Check.objects.get_or_create()
        check.payment_number = p.payment_number
        check.save()
    p.save()
    return p

    # Create Events

for event in event_info:
    e = Event.objects.get_or_create()
    e.name = event[0]
    e.type = event[1]
    e.date = event[2]
    e.begin = event[3]
    e.end = event[4]
    # Create tickets and customers
    for i in range(20):
        c = Customer.objects.get_or_create()
        first = ""
        last = last_name[0]
        if random.randint(1):
            first = male_file.next()[0]
        else:
            first = female_file.next()[0]
        c.name = first + last
        c.email = c.name + " @google.com"

        t = Ticket.objects.get_or_create()
        t.event_id = e.event_id
        t.customer_id = c.customer_id

        p = create_payment()
        t.payment_number = p.payment_number

        c.save()
        t.save()

    e.save()

# Create Vendors
for vendor in vendors:
    v = Vendor.objects.get_or_create()
    vhold = vendor[1:]
    v.name = vhold[0]
    v.email = vhold[1]
    v.phone = vhold[2]
    v.address = vhold[3]
    # Create Space
    s = Space.objects.get_or_create()
    s.rent = "500"
    v.space = s.space_id
    s.save()
    v.save()

# Create Staff
# Create Positions
for position in positions:
    phold = positions.next()[1:]
    p = Position.objects.get_or_create()
    s = Staff.objects.get_or_create()
    first = ""
    last = last_name[0]
    if random.randint(1):
        first = male_file.next()[0]
    else:
        first = female_file.next()[0]
    s.name = first + last
    s.save()

    p.position = phold[0]
    p.description = phold[1]
    p.salary = phold[2]
    p.staff_id = s.staff_id
    p.save()


