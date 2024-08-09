from django.db import models
from django.conf import settings

class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    response = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document = models.FileField(upload_to='processing/')
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.document.name
    
