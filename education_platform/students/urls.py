from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path(
        'register/',
        views.StudentRegisterView.as_view(),
        name='student_register'
    ),
]
