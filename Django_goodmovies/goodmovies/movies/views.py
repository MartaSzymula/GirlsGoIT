from django.shortcuts import render
from django.http import HttpResponse
import datetime
from movies.models import Movie

def hello_world(request):

    my_context = {
        "time": datetime.datetime.now()
    }
    return render(request, template_name="hello.html", context=my_context)


def movies(request):
    my_context = {
        "movies": Movie.objects.all()
    }
    return render(request, template_name="movies.html", context=my_context)


def index(request):
    return render(request, template_name="base.html")

    
def subpage(request):
    return render(request, template_name="subpage.html")


def index(request):
    return render(request, template_name="index.html")


def movie_list(request):
    my_context = {"movies": Movie.objects.all() }

    return render(request, template_name="movie_list.html", context=my_context)