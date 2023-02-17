from django.urls import path, re_path
from . import views

app_name = 'user'

urlpatterns = [
    path("register/", views.OrganizerCreateView.as_view() ,name='register'),
    re_path(r"^(?P<pk>)\d+/$", views.OrganizerDetailView.as_view() ,name='profile'),

]