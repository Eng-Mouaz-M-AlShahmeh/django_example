from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hi/', views.say_hi)
]
