from django.contrib import admin
from accounts.models.user import User
from accounts.models.student import Student
from accounts.models.teacher import Teacher
from accounts.models.parent import Parent

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)