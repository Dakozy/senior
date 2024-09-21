from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date



class Senior(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    image = models.ImageField(upload_to="profile_pics", default="img.png")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    dob = models.DateField(default='2000-01-01')
    address = models.CharField(max_length=300, default="Creek Road")
    phone = models.CharField(max_length=15, default="8099765654")
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("senior-detail", args=[self.slug])
    
    class Meta:
        ordering = ["-updated"]

    def __str__(self):
        return self.full_name


