from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = "judge" 

CUSTOM_PATH = '/question/'
OTH_DIR = 'C:/Users/Admin/Documents/openJudge/open_judge/questions/1/statement'

urlpatterns = [
    path('workspace/', views.workspace, name='workspace'), 
    path('handle/', views.handler, name='handle'),
] + static(CUSTOM_PATH, document_root=OTH_DIR)
