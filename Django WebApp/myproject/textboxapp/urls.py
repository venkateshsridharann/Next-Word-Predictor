from django.urls import path
from . import views

urlpatterns = [
    path('', views.textbox_page, name='textbox_page'),
]