from django.shortcuts import render
from .models import Experience, Education, Resume

# Create your views here.
def home(request):
    """
    Renders the Resume app home template
    """
    resume_qs = Resume.objects.first()
    context = {'res': resume_qs}
    return render(request, 'resume/home.html', context)
