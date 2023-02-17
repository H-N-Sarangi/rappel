from django.db import models

# Create your models here.
class OrganizerProfile(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.fname.title()} {self.lname.title()}'

class UserProfile(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    registration_no = models.CharField(unique=True, max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.fname.title()} {self.lname.title()}'
