from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register_student/', views.register_student, name='register_student'),
    path('all_student_list/', views.all_student_list, name='all_student_list'),
]
    

