from django.urls import path, include
from rest_framework import routers
from Books import views


router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)
router.register(r'orders', views.OrdersViewSet)
urlpatterns = [
    path('', include(router.urls)),
]