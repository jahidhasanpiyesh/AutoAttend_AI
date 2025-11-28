from django.db import models
from django.utils import timezone

# Create your models here.

class Student_Registration(models.Model):
    stu_id = models.CharField(max_length=30, unique=True, help_text="Unique Id Assigned to Each Student")
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,unique=True)
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='student_images/')
    is_active = models.BooleanField(default=True)
    # registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.stu_id})"



class CameraConfiguration(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Give a name to this camera configuration")
    camera_source = models.CharField(max_length=255, help_text="Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)")
    threshold = models.FloatField(default=0.6, help_text="Face recognition confidence threshold")

    def __str__(self):
        return self.name