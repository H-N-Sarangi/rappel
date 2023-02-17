from django.urls import path, re_path
from . import views


app_name = 'note'

urlpatterns = [
    path("" , views.IndexView.as_view(), name='home-page'),
    path("allevents/" , views.NoticeListView.as_view(), name='all-events'),
    re_path(r"^allevents/(?P<pk>\d+)/$", views.NoticeDetailView.as_view(), name='event-details'),
    re_path(r"^allevents/create/$", views.NoticeCreateView.as_view(), name='event-creation'),
    re_path(r"^allevents/(?P<pk>\d+)/update/$", views.NoticeUpdateView.as_view(), name='event-update'),
    re_path(r"^allevents/(?P<pk>\d+)/delete/$", views.NoticeDeleteView.as_view(), name='event-delete'),


]