
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main, name="main"),
    path('enrollments/', views.enrollment_create, name='enrollment-create'),
]
