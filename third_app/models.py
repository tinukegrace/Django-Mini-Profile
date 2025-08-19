from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="photos/",default="image-upload")
    welcome_text =models.TextField()
    aspiration = models.TextField()
    
    
    def __str__(self):
        return self.name
    


class Skill(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tools = models.TextField()
    
    def __str__(self):
        return self.title
    
