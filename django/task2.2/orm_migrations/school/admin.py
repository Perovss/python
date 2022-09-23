from django.contrib import admin

from .models import Student, Teacher

class TeacherInline(admin.TabularInline):
    model = Teacher.student.through
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['name', 'subject']
    exclude = ('student', )
