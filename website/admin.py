from django.contrib import admin
from .models import Record

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email", "address", "city", "state", "zipcode", "created_at")

admin.site.register(Record, RecordAdmin)


