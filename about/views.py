from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def index(request):
    about_us_list = About.objects.all()
    context = {
        'about': about_us_list[0] if len(about_us_list) > 0 else []
    }

    return render(request, 'about/index.html', context=context)
