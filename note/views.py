from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'note/index.html'

class NoticeListView(ListView):
    template_name = 'note/notice.html'
    model = models.Notice

class NoticeDetailView(DetailView):
    template_name = 'note/detail.html'
    model = models.Notice

class NoticeCreateView(CreateView):
    model = models.Notice
    fields = '__all__'
    template_name_suffix = '_form'

class NoticeUpdateView(UpdateView):
    model = models.Notice
    fields = '__all__'
    template_name_suffix = '_form'


class NoticeDeleteView(DeleteView):
    model = models.Notice
    success_url = reverse_lazy('note:all-events')
    template_name = 'note/notice_del.html'

#crete subevent views