from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home,name='home'),
    path('readers/',readers,name='readers'),
    path('save',save_student,name='save'),
]