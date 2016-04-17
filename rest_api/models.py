from django.db import models


class Customer(models.Model):
    """
        This is the data for Customer
    """

    customer_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Ticket(models.Model):

    ticket_number = models.CharField(max_length=100, primary_key=True)
    # time =
    payment_number = models.ForeignKey('Payment', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)


class Event(models.Model):

    event_id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    date = models.DateField()
    begin = models.TimeField()
    end = models.TimeField()


class Seating(models.Model):

    seating_number = models.CharField(max_length=100, primary_key=True)
    ticket_number = models.ForeignKey('Ticket', on_delete=models.CASCADE)


class Payment(models.Model):

    payment_number = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=10)


class Card(models.Model):

    payment_number = models.ForeignKey('Payment', on_delete=models.CASCADE, primary_key=True)
    card_type = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)


class Check(models.Model):

    payment_number = models.ForeignKey('Payment', on_delete=models.CASCADE, primary_key=True)
    check_number = models.CharField(max_length=100)


class Cash(models.Model):

    payment_number = models.ForeignKey('Payment', on_delete=models.CASCADE, primary_key=True)


class Vendor(models.Model):

    vendor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    space_id = models.ForeignKey('Space', on_delete=models.CASCADE)


class Space(models.Model):

    space_id = models.CharField(max_length=100, primary_key=True)
    rent = models.CharField(max_length=100)


class Staff(models.Model):

    staff_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)


class Position(models.Model):

    position_id = models.CharField(max_length=100, primary_key=True)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    staff_id = models.ForeignKey('Staff', on_delete=models.CASCADE)

