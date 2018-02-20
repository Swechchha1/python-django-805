from django.contrib import admin
from django.conf.locale.es import formats
from .models import Experience, Education, Resume

# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)
