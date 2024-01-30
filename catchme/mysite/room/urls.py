from django.urls import path
from django.contrib.auth import views as auth_views
from .views import room_views
app_name = "room"
urlpatterns = [
    path('api/room_info/',room_views.RoomListView.as_view(), name="roomListView"),
    path('',room_views.index,name ="index"),
    path('<int:r_no>/',room_views.selectedRoom,name="selectedRoom"),
    path('api/<int:r_no>/',room_views.SelectedRoomView.as_view(), name= "selectedRoomView"),
]