from django.shortcuts import render, redirect
from .models import Portfolio, Skill
from .forms import Contact

def home(request):
    portfolio = Portfolio.objects.first()
        
    if portfolio:
        skills = Skill.objects.filter(portf=portfolio)
    else:
        skills = []
            
    context = {
        'portfolio': portfolio,
        'skills': skills,
    }
    return render(request, 'home.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
        else:
            print("Form is not valid:", form.errors)
    else:
        return redirect('home')

def success_view(request):
    return render(request, 'success.html')
