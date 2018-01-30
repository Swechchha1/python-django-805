from django.shortcuts import render

def home(request):
    '''
    Renders a home page
    '''
    greeting = "uStudy- the best study site in the world!"
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    context = {"our_greeting":greeting, "day_list":days_of_week}
    return render(request, 'home.html', context)
