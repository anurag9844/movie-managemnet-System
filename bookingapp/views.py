from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import MovieBookingForm
from .models import Movie, MovieBooking
# Create your views here.


def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def movie_booking(request):
    if request.method == "POST":
        form = MovieBookingForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    form = MovieBookingForm()
    return render(request, 'moviebooking.html', {'form':form})

def movie_list(request):
    movies = Movie.objects.all()
    moviebooking = MovieBooking.objects.all()
    return render(request, 'index.html', {'movies':movies, 'moviebooking':moviebooking})
