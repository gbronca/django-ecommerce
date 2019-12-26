from django.urls import path
from . import views
# from django.views.generic import FormView

app_name = 'accounts'

urlpatterns = [
    path('signup', views.UserRegistrationForm, name='signup'),
]