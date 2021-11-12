from Books.models import Book, Order
from rest_framework import serializers


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'type']
class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['customerName', 'bookId']