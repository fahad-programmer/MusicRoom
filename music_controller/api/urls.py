from django.urls import path
from .views import *

urlpatterns = [
    path('home', RoomView.as_view(), name="RoomView"),
    path('create-room', CreateRoomView.as_view(), name="CreateRoom")
]
