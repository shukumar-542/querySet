from django.contrib import admin

from school.models import Student,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
      list_display = ['id', 'name','roll','city','result','pass_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
      list_display = ['id', 'name','empid','city','salary','join_date']

