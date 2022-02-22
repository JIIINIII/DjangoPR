from django.urls import path
from userApp import views

urlpatterns = [
    # http://127.0.0.1:8000/user/index
    path('index/',views.index)
]