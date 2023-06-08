from django.urls import path
from .views import movie_list, user_registration, movie_booking
urlpatterns = [
    path('', movie_list, name="index"),
    path('registration/', user_registration, name='user_registration'),
    path('movie/booking', movie_booking, name="movie_booking"),
]
