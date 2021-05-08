from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notify/<int:notify_id>/', views.detail, name='detail'),
]
