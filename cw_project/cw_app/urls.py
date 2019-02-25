from django.urls import path

from . import views

urlpatterns = [
    path('movies/synopsis/', views.synopsisFunc, name='synopsis'),
    path('movies/details/', views.detailsFunc, name='details'),
    path('', views.index, name='index'),
]
