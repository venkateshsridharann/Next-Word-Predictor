from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form, name= 'predict'),
    path('ajax/', views.ajax_view, name='ajax_view'),
 
]