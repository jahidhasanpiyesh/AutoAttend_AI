from django.shortcuts import redirect, render
from .models import Student_Registration
# Create your views here.

# ----------------------------------------View for rendering the home page---------------------------
def home(request):
    return render(request, 'index.html')

# --------------------------------------View for rendering the student registration page---------------------------
def register_stu(request):
    if request.method == 'POST':
        stu_id = request.POST.get('stu_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        designation = request.POST.get('designation')
        department = request.POST.get('department')

        profile_image = request.FILES.get('profile_image')
        image_data = request.POST.get('image_data')

        student_registration = Student_Registration(
            stu_id=stu_id,
            name=name,
            email=email,
            phone_number=phone_number,
            designation=designation,
            department=department,
            profile_image=profile_image,
            image_data=image_data,
            is_active = True
        )
        student_registration.save()
        massage = "Student Registered Successfully"
        return redirect('register_success')
    return render(request, 'register_stu.html')

# ----------------------------------------View for rendering the registration success page---------------------------
def register_success(request):
    return render(request, 'register_success.html')

# ----------------------------------------View for rendering the login page---------------------------
def login(request):
    return render(request, 'login.html')

# ----------------------------------------View for rendering the student list page---------------------------
def stu_list(request):
    return render(request, 'stu_list.html')

# ----------------------------------------View for rendering the attendance list page---------------------------
def attendance_list(request):
    return render(request, 'attendance_list.html')