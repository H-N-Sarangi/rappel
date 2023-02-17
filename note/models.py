from django.db import models
from django.urls import reverse


# Create your models here.
class Notice(models.Model):
    topic = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()
    card_img = models.ImageField(blank=True, upload_to='card_imgs')

    def __str__(self) -> str:
        return self.topic.title()

    def get_absolute_url(self):
        return reverse('note:all-events',)

class SubNotice(models.Model):
    topic = models.CharField(max_length=50)
    date = models.DateField()
    desc = models.TextField()
    main_event = models.ForeignKey(Notice, related_name='subevents', on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.topic.title()
    
    def get_absolute_url(self):
        return reverse('note:all-events',)