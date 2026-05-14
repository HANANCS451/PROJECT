from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meals/', views.meals_list, name='meals_list'),
    path('meal/<int:id>/', views.meal_detail, name='meal_detail'),
    path('add/',  views.add_meal,  name='add_meal'),
]