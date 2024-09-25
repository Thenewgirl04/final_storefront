from django.urls import path
from . import views

print("yay")
 
urlpatterns = [
    path('hello/', views.say_hello)
]