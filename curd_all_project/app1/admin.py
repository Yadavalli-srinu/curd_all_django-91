from django.contrib import admin

from app1.models import student_model

class student_admin(admin.ModelAdmin):
    list_display=["name","age","mobile","email","dept","join_date"]
admin.site.register(student_model,student_admin)
