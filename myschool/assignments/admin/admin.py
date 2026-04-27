from django.contrib import admin
from assignments.models.assignment import Assignment
from assignments.models.submission import Submission

admin.site.register(Assignment)
admin.site.register(Submission)