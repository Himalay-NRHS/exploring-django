from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_page, name='feedback'),
    path('submit/', views.submit_feedback, name='submit_feedback'),
]