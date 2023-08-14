from django.urls import path
from pageOne.views import index

urlpatterns = [
    path('', index)
]