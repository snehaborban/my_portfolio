from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    bio1 = models.CharField(max_length=500)
    bio2 = models.CharField(max_length=500)
    bio3 = models.CharField(max_length=500)
    img = models.ImageField(upload_to='my_images/')
    about1 = models.TextField()
    about2 = models.TextField()
    aboutimg = models.ImageField(upload_to='my_images/')
    contactInfo = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    location = models.CharField(max_length=500)

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    portf = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='skills')
    category = models.CharField(max_length=50) # e.g., 'Languages', 'Frameworks'
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, default='fas fa-code')

    def __str__(self):
        return f"{self.category}: {self.name}"
