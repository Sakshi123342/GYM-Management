from django.shortcuts import render
from .models import ContactMessage

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def trainers(request):
    return render(request,'trainers.html')

def membership(request):
    return render(request,'membership.html')

def bmi(request):
    return render(request,'bmi.html')

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(
            request,
            'contact.html',
            {'success': 'Your message has been sent successfully!'}
        )

    return render(request, 'contact.html')