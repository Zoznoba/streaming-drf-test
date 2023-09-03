from django.shortcuts import render
from models import Trip
# Create your views here.

class ScheduleView(ListView):
    model = Trip
    context_object_name = ''
    template_name=''