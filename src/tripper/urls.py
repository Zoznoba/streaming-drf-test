from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('schedule/', views.ScheduleView.as_view())
]
