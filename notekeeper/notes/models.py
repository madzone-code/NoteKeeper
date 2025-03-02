from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Topic(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Всем'),
        ('private', 'Только себе'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES)
    topic = models.ForeignKey(Topic, related_name='notes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notes_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Новое поле author

    def __str__(self):
        return self.title
