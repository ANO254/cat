from django.shortcuts import render


def Home(request):
    return render(request,'index.html')


def About(request):
    return render(request,'about.html')


def Design(request):
    return render(request,'design.html')


def Contact(request):
    return render(request,'contact.html')


def Shop(request):
    return render(request,'shop.html')