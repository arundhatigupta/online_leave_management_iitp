from django.contrib import admin

from users.models import Student, ApprovingAuthority, UserAccount

admin.site.register(Student)
admin.site.register(ApprovingAuthority)
admin.site.register(UserAccount)