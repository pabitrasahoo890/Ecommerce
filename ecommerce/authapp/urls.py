from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', Signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('activate/<uidb64>/<token>', ActivateAccountView.as_view(), name='activate'),
]
