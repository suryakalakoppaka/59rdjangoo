from django.contrib import admin
from app1.models import students

class student_admin(admin.ModelAdmin):
    list_display=['std_id','std_name','std_age']
    ordering=['std_id']
admin.site.register(students,student_admin)
