from django.shortcuts import render

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def about_us(request):
    """ A view to return the about us page """
    return render(request, 'home/about.html')

def privacy(request):
    """ A view to return the privacy policy """
    return render(request, 'home/privacy.html')