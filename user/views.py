from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
# Create your views here.
class OrganizerCreateView(CreateView):
    model = OrganizerProfile
    fields = '__all__'
    template_name = 'user/users_form.html'
    
class ParticipantCreateView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'user/users_form.html'


class OrganizerDetailView(DetailView):
    model = OrganizerProfile
    template_name = 'user/user_profile.html'