from django.urls import path
from . import views

urlpatterns = [
    path('', views.WheatherView.as_view())
]
