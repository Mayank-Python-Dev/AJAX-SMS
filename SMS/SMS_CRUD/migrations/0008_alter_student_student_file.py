# Generated by Django 3.2.6 on 2021-08-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_CRUD', '0007_alter_student_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_File',
            field=models.FileField(blank=True, null=True, upload_to='static/media'),
        ),
    ]