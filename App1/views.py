from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register_stu(request):
    return render(request, 'register_stu.html')

def login(request):
    return render(request, 'login.html')

def stu_list(request):
    return render(request, 'stu_list.html')

def attenance_list(request):
    return render(request, 'attendance_list.html')