from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("allcars/", views.allcars, name="allcars"),
    path("allcars/orders/<int:id>", views.car_orders, name="car_orders"),
    path("allcars/order_lines/<int:id>", views.order_lines, name="order_lines"),
    path("orders/", views.OrdersListView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order_details"),
    path("search/", views.search, name="search")


]

