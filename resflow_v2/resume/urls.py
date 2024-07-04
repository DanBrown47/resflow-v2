from django.urls import path
from .views import ResumeCreateView

urlpatterns = [
    path('upload/', ResumeCreateView.as_view(), name='resume-upload'),
    ]
