from django.db import models

# Create your models here.
class Tattoo(models.Model):
    image = models.ImageField(upload_to='tattoos/')
    created_at = models.DateTimeField(auto_now_add=True)

  