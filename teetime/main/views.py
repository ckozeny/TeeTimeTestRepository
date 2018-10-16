from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def membership(request):
    return render(request, 'main/membership.html')


def scheduling(request):
    return render(request, 'main/scheduling.html')


def events(request):
    return render(request, 'main/events.html')


def contact(request):
    return render(request, 'main/contact.html')