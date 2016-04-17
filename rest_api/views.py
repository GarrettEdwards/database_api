from django.shortcuts import render
from rest_api.serializers import *
from rest_framework import viewsets


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TicketViewSet(viewsets.ModelViewSet):
    name = 'ticket'
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class EventViewSet(viewsets.ModelViewSet):
    name = 'event'
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SeatingViewSet(viewsets.ModelViewSet):
    name = 'seating'
    queryset = Seating.objects.all()
    serializer_class = SeatingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    name = 'payment'
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CardViewSet(viewsets.ModelViewSet):
    name = 'card'
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CheckViewSet(viewsets.ModelViewSet):
    name = 'check'
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class CashViewSet(viewsets.ModelViewSet):
    name = 'cash'
    queryset = Cash.objects.all()
    serializer_class = CashSerializer


class VendorViewSet(viewsets.ModelViewSet):
    name = 'vendor'
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    name = 'space'
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class StaffViewSet(viewsets.ModelViewSet):
    name = 'staff'
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class PositionViewSet(viewsets.ModelViewSet):
    name = 'position'
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
