from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('home/',views.drop,name='home'),

    path('',TemplateView.as_view(template_name='welcome.html'),name='welcome'),
]
