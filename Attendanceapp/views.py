from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_student(request):
    return render(request, 'register_student.html')