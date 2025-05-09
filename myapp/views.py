from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def hobbies(request):
    return render(request, 'hobbies.html')

def contact(request):
    return render(request, 'contact.html')
