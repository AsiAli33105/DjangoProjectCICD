from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('LandingPage', views.LandingPage, name='login'),
#path('records/', views.records, name='records'),
#path('contacts/', views.contacts, name='contacts'),
]