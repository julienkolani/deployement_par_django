from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('somme10/', views.sum_numbers10, name='sum_numbers10'),
    path('somme100/', views.sum_numbers100, name='sum_numbers100'),
    path('somme1000/', views.sum_numbers1000, name='sum_numbers1000'),
    path('somme10000/', views.sum_numbers10000, name='sum_numbers10000'),
]
