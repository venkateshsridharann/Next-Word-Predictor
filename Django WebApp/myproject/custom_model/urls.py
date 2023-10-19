from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.textbox_page, name='textbox_page'),
    path('', views.input_form, name= 'predict'),
    path('ajax/', views.ajax_view, name='ajax_view'),
 
]