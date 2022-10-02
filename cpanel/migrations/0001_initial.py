# Generated by Django 4.1.1 on 2022-10-02 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('admission_date', models.DateField()),
                ('class_level', models.CharField(choices=[('s1', 'S.1'), ('s2', 'S.2'), ('s3', 'S.3'), ('s4', 'S.4'), ('s5', 'S.5'), ('s6', 'S.6')], max_length=3, verbose_name='Class')),
                ('withdrawal_reason', models.TextField(blank=True, default='N/A')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('sur_name', models.CharField(max_length=30, verbose_name='Sur Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('std_no', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Student Number')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=2)),
                ('age', models.PositiveIntegerField()),
                ('address_of_parents', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VistorsBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('purpose_of_visit', models.TextField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date_visited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PunishmentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=2)),
                ('age', models.PositiveIntegerField()),
                ('class_of_offender', models.CharField(choices=[('s1', 'S.1'), ('s2', 'S.2'), ('s3', 'S.3'), ('s4', 'S.4'), ('s5', 'S.5'), ('s6', 'S.6')], max_length=3)),
                ('offence', models.TextField()),
                ('punishment', models.TextField()),
                ('by_whom', models.CharField(max_length=30)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('punishment_date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpanel.student')),
            ],
        ),
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('events_reported', models.TextField()),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logbook_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttendenceRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MON', 'MONDAY'), ('TUE', 'TUESDAY'), ('WED', 'WEDNESDAY'), ('THUR', 'THURSDAY'), ('FRI', 'FRIDAY')], max_length=10)),
                ('attended', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=10)),
                ('admission_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpanel.admission')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpanel.student')),
            ],
        ),
        migrations.AddField(
            model_name='admission',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_admission_foregin', to='cpanel.student'),
        ),
    ]
