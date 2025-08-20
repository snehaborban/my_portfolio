from django.contrib import admin
from .models import Portfolio,Skill
from .models import ContactForm

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(ContactForm)