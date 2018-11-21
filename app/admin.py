from django.contrib import admin

from app.models import Leave, LeaveApprovingFaculty, LeaveApprovingWarden

admin.site.register(Leave)
admin.site.register(LeaveApprovingFaculty)
admin.site.register(LeaveApprovingWarden)