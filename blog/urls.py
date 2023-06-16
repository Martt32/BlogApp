from django.urls import path
from . import views


urlpatterns=[
    path('', views.blogCreateView, name='create'),
    path('<int:pk>/', views.blogView, name='retrieve'),

]