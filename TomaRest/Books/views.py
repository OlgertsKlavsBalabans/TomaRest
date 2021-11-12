from django.shortcuts import render

# Create your views here.
from Books.models import Book,Order
from rest_framework import viewsets
from rest_framework import permissions
from Books.serializers import BooksSerializer,OrdersSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]