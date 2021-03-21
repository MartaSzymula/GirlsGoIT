from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
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

    
def profile_view(request):
    return render(request, template_name="my_profile.html")


def index(request):
    return render(request, template_name="index.html")


def movie_list(request):
    my_context = {"movies": Movie.objects.all() }

    return render(request, template_name="movie_list.html", context=my_context)

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, template_name="registration/signup_complete.html")
    else:
        form = UserCreationForm()
    return render(request, template_name="registration/signup_form.html", context={'form':form})
