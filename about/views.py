from django.shortcuts import render
from .models import About

def index(request):
    abouts = About.objects.all()
    context = {
        'about': abouts[0] if len(abouts) > 0 else []
    }
    return render(request, 'about/index.html', context=context)
