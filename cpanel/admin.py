from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django import forms
from cpanel.models import Admission, AttendenceRegister, LogBook, PunishmentBook, Student, VistorsBook
# Register your models here.

class SimsAdmin(admin.AdminSite):
    site_header = "OLD KAMPALA ADMINISTRATION"
    site_title = "ADMIN"
    index_title= "Old Kampala Senior Secondary School"

sims_admin = SimsAdmin(name='sims')
sims_admin.register(Group, GroupAdmin)
sims_admin.register(User, UserAdmin)

class StudentChoicesField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.sur_name} {obj.first_name}"

class AdmissionChoicesField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"ADMISSION({obj.id})"
@admin.register(Student, site=sims_admin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('sur_name', 'first_name', 'date_of_birth', 'std_no', 'sex', 'age', 'address_of_parents')
    list_display_links = ('sur_name',)
    search_fields = ['sur_name', 'first_name', 'std_no']

@admin.register(Admission, site=sims_admin)
class AdimissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'age', 'class_level', 'admission_date', 'withdrawal_reason')
    search_fields = ['id', 'class_level']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            return StudentChoicesField(queryset=Student.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

    def student_name(self, obj):
        return f"{ obj.student.sur_name } { obj.student.first_name }"

    def age(self, obj):
        current_yr = datetime.now().year
        stud_yr = str(obj.student.date_of_birth)[:4]
        return f"{ current_yr - int(stud_yr)}"
@admin.register(VistorsBook, site=sims_admin)
class VisitorsBooKAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'purpose_of_visit', 'remarks', 'date_visited')

@admin.register(LogBook)
class LogBookAdmin(admin.ModelAdmin):
    list_display = ('log_date', 'events_reported', 'signature')

@admin.register(PunishmentBook, site=sims_admin)
class PunishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'sex', 'class_of_offender', 'offence', 'punishment', 'by_whom', 'punishment_date')
    list_filter = ('offence', 'punishment')
    search_fields = ['offense', 'punishment']

@admin.register(AttendenceRegister, site=sims_admin)
class AttendenceRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'admission_no', 'day', 'attended')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'admission_number':
            return AdmissionChoicesField(queryset=Admission.objects.all())
        elif db_field.name == 'name':
            return StudentChoicesField(queryset=Student.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

    def student_name(self, obj):
        return f"{obj.name.sur_name} {obj.name.first_name}"
    
    def admission_no(self, obj):
        return f"{obj.admission_number.id}"