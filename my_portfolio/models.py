from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    bio1 = models.CharField(max_length=500,blank=True, null=True)
    bio2 = models.CharField(max_length=500,blank=True, null=True)
    bio3 = models.CharField(max_length=500,blank=True, null=True)
    img = models.ImageField(upload_to='my_images/',blank=True, null=True)
    about1 = models.TextField(blank=True, null=True)
    about2 = models.TextField(blank=True, null=True )
    aboutimg = models.ImageField(upload_to='my_images/',blank=True, null=True)
    contactInfo = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=13,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=500,blank=True, null=True)

class ContactForm(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    portf = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True) # e.g., 'Languages', 'Frameworks'
    name = models.CharField(max_length=50, blank=True, null=True)
    icon_class = models.CharField(max_length=50, default='fas fa-code', blank=True, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}"
