from django.urls import path, include
from . import views

app_name = "judge" 

urlpatterns = [
    path('workspace/', views.workspace, name='workspace'), 
    path('handle/', views.handler, name='handle')
]
