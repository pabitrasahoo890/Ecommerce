from django.urls import path
from .views import *
urlpatterns = [
    path('', Index, name='index'),
    path('contact', Contactus, name='contact'),
    path('about', About, name='about'),
    path('checkout/', checkout, name='checkout'),
    path('handlerequest/', handlerequest, name="HandleRequest"),
]