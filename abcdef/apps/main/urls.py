from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/<key>/', views.add, name='add'),
]
