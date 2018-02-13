from django.shortcuts import render

def home(request):
    '''
    Renders a home page
    '''
    return render(request, 'home.html', context=None)

def portfolio(request):
    '''
    Renders a portfolio page
    '''
    return render(request, 'portfolio.html', context=None)

def resume(request):
    '''
    Renders a resume page
    '''
    return render(request, 'resume.html', context=None)

def contact(request):
    '''
    Renders a contact page
    '''
    return render(request, 'contact.html', context=None)       
