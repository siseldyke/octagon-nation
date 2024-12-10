from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .models import Event

def home(request):
    return render(request, 'home.html')

def event_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

# def event_detail(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     return render(request, 'events/event-detail.html', {'event': event})