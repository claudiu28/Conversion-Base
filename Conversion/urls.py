from django.urls import path
from . import views as vws
urlpatterns = [
    path('', vws.home, name='home'),
]