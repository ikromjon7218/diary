from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Profil(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # username, password

    last_activity = models.DateTimeField(null=True, blank=True)
    def update_activity(self):
        self.last_activity = timezone.now()
        self.save()

    def __str__(self):
        return self.name
