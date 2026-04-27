from django.contrib import admin
from academics.models.field import Field
from academics.models.level import Level
from academics.models.course import Course
from academics.models.enrollment import Enrollment
from academics.models.mark import Mark
from academics.models.absence import Absence

admin.site.register(Field)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Mark)
admin.site.register(Absence)