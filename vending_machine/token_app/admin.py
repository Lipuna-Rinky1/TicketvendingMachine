from django.contrib import admin
from .models import Doctor, Department, Token, User
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Token)
admin.site.register(User)