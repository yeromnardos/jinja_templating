from django.urls import path
from jinjaapp import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('Gallery/', views.Gallery, name='gallery')
]
