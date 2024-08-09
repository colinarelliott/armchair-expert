from django.db import models

# User model identifies user, associates with chat and document models
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='../processing/')
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return self.document.name
    
