from django.contrib import admin
from ImageApp.models import MyPhoto
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)
admin.site.register(MyPhoto)
