from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def home(request):
    """
    Renders the Resume app home template
    """
    education_qs = Education.objects.all()
    experience_qs = Experience.objects.all()
    context = {'edu': education_qs, 'exp':experience_qs}
    return render(request, 'resume/home.html', context)
