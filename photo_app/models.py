from django.db import models
from user_app.models import UserModel

# Create your models here.
class Photomodel(models.Model):
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='upload_pic')
    caption = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
