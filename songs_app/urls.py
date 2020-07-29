from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('home/',TemplateView.as_view(template_name='home.html'),name='home'),
    path('',TemplateView.as_view(template_name='welcome.html'),name='welcome'),
]
