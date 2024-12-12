from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Event
from .forms import UserProfileForm

class Home(LoginView):
    template_name = 'home.html'

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

class EventUpdate(UpdateView):
    model = Event
    fields = ['attendees', 'location', 'date']
    success_url = '/events/'

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'

@login_required
def profile_view(request):
    return render(request, 'profile/index.html')

@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'user_profile.html', {'form': form, 'user_profile': user_profile})    