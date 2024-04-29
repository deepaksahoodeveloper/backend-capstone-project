from django.contrib import admin 
from django.urls import path 
from .views import index , MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView, BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView
  
urlpatterns = [ 
     path('', index, name='index'),
     path('menu/', MenuListCreateAPIView.as_view()),
     path('menu/<int:pk>', MenuRetrieveUpdateDestroyAPIView.as_view()),
     path('booking', BookingListCreateAPIView.as_view()),
     path('booking/<int:pk>', BookingRetrieveUpdateDestroyAPIView.as_view()),
]