from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom/', include('custom_model.urls')),
    path('pretrained/', include('pretrained_model.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
