from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .models import Event

def home(request):
    return render(request, 'home.html')

def event_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'attendees', 'location', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/events/'