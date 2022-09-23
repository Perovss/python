# Generated by Django 4.1 on 2022-09-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='student', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
