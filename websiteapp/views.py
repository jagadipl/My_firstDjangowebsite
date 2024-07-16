from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'websiteapp/index.html')

def about(request):
    return render(request,'websiteapp/about.html')

def contact(request):
    return render(request,'websiteapp/contact.html')

def gallery(request):
    return render(request,'websiteapp/gallery.html')

def interest(request):
    return render(request,'websiteapp/interest.html')