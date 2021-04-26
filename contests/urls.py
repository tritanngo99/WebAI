from django.urls import path
from . import views

urlpatterns = [
    path('contest/', views.view_contest, name='view_contest'),
    path('contest/<int:contest_id>/', views.detail, name='detail'),
    path('exercise/<int:exercise_id>/', views.submit_exercise, name='submit_exercise'),
]