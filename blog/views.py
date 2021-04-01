from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from time import strftime

from .models import About

def about(request):
    return render(request,
        'blog/about.html', 
        {
            'now': strftime('%c'),
        }
    )

def tips(request):
    return render(request,
        'blog/techtips+css.html', 
        {
            'now': strftime('%c'),
        }
    )




