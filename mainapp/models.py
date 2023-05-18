from django.db import models
from userapp.models import Profil

class Error(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name[:10]

class Daily(models.Model):
    pray = models.SmallIntegerField(null=True, blank=True)
    event = models.CharField(max_length=1000, null=True, blank=True)
    bed_time = models.DurationField(null=True, blank=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.bed_time)

class Note(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, null=True)
    time = models.DateTimeField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    def __str__(self):
        return self.name[:20]

