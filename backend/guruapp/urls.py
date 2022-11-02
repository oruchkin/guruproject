from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name='index'),
    path("city/", views.City_list.as_view()),
    path("city/<int:pk>/", views.City_detail.as_view()),
    path("city/<int:pk>/street/", views.City_street.as_view()),
    path("shop/", views.New_shop.as_view()),
]




