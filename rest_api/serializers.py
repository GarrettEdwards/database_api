from rest_api.models import Customer, Ticket, Event, Seating, Payment, Card, Check, Cash, Vendor, Space, Staff, Position
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'email')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('ticket_number', 'time', 'payment_number', 'event_id', 'customer_id')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'type', 'date', 'begin', 'end')


class SeatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seating
        fields = ('seating_number', 'ticket_number')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_number', 'type', 'amount')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('payment_number', 'card_type', 'card_number', 'zip')


class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = ('payment_number', 'check_number')


class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cash
        fields = 'payment_number'


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('vendor_id', 'name', 'email', 'phone', 'address', 'space_id')


class SpaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Space
        fields = ('space_id', 'rent')


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ('staff_id', 'name')


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('position_id', 'position', 'description', 'salary', 'staff_id')
