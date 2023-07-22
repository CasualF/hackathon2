from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Room(models.Model):
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    name = models.CharField(max_length=120)
    online = models.ManyToManyField(User, blank=True)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} {self.get_online_count()}'


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -> {self.body}'