import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CLASS_CHOICES = (
        ('s1', 'S.1'), ('s2', 'S.2',), ('s3', 'S.3',),  ('s4', 'S.4'), ('s5', 'S.5'), ('s6', 'S.6')
    )
GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'))
DAYS_CHOICES = (('MON', 'MONDAY'), ('TUE', 'TUESDAY'), ('WED', 'WEDNESDAY'), ('THUR', 'THURSDAY'), ('FRI', 'FRIDAY'))
ATTENDENCE_CHOICES = (('yes', 'YES'), ('no', 'NO'))
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30, verbose_name="Sur Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    std_no = models.UUIDField(verbose_name="Student Number", default=uuid.uuid4, editable=False)
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    address_of_parents = models.CharField(max_length=100)

class Admission(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="student_admission_foregin")
    admission_date = models.DateField()
    class_level = models.CharField(verbose_name="Class", choices=CLASS_CHOICES, max_length=3)
    withdrawal_reason = models.TextField(default="N/A", blank=True)


class VistorsBook(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    purpose_of_visit = models.TextField()
    remarks = models.TextField(blank=True, null=True)
    date_visited = models.DateTimeField(auto_now_add=True)


class LogBook(models.Model):
    log_date = models.DateField(verbose_name="Date", auto_now_add=True)
    events_reported = models.TextField()
    signature = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logbook_user_id")

class PunishmentBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    class_of_offender = models.CharField(max_length=3, choices=CLASS_CHOICES)
    offence = models.TextField()
    punishment = models.TextField()
    by_whom = models.CharField(max_length=30)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    punishment_date = models.DateField(auto_now_add=True)

class AttendenceRegister(models.Model):
    admission_number = models.ForeignKey(Admission, on_delete=models.CASCADE)
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS_CHOICES)
    attended= models.CharField(max_length=10, choices=ATTENDENCE_CHOICES)