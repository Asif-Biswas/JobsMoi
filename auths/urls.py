from django.urls import path, include

from . import views

urlpatterns = [
    path("login", views.signin, name="login"),
    path("register", views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
]