from django.urls import path 
from Task import views


urlpatterns=[
    path("", views.home, name="home"),
    path("product", views.product, name="product"),
    path("insert", views.insert, name="insert"),
    path("goods", views.goods, name="goods"),
    path("move", views.move, name="move")
]