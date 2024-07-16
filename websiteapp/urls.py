from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('gallery/',views.gallery, name='gallery'),
    path('interest/',views.interest, name='interest')
    
    
    
    
    ]