from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'themes/index.html')


def dropdown(request):
    return render(request, 'themes/dropdown.html')
    
def elements(request):
    return render(request, 'themes/elements.html')
    
def services(request):
    return render(request, 'themes/services.html')

def about(request):
    return render(request, 'themes/about.html')
    
def contact(request):
    return render(request, 'themes/contact.html')
    


    
     