from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')

        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(
            request,
            'home/contact.html',
            {'success': True}
        )

    return render(request, 'home/contact.html')