from django.db import models

# Create your models here.
class Tattoo(models.Model):
    image = models.ImageField(upload_to='tattoos/')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Guide(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
class GuideImages(models.Model):
    guide = models.ForeignKey(Guide, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='guide/')
    
    def __str__(self):
        return f"image for {self.guide.name}"

  