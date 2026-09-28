from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('membership/',views.membership,name='membership'),
    path('trainers/',views.trainers,name='trainers'),
    path('bmi/',views.bmi,name='bmi'),
    path('contact/',views.contact,name='contact'), 
]