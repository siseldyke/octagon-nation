from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from .forms import EventForm
from .forms import UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied



class Home(LoginView):
    template_name = 'home.html'

@login_required
def event_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'attendees', 'location', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/events/'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['attendees', 'location', 'date']
    success_url = '/events/'
    def get_object(self, queryset=None):
        
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:
             raise PermissionDenied("You are not allowed to edit this event.")
        return obj

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'
    def get_object(self, queryset=None):
        
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:
             raise PermissionDenied("You are not allowed to delete this event.")
        return obj
        
@login_required
def profile_view(request):
    return render(request, 'profile/index.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   