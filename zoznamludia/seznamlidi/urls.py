from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/vytvorit',views.create, name='create'),
    path('/<int:pk>/', views.detail, name='detail'),
]

