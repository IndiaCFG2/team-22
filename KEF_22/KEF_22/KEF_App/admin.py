from django.contrib import admin
from .models import Teacher
from .models import Teacher_Query
from .models import Assesment

admin.site.site_header = "Key Education Foundation"
admin.site.site_title = "Key Education Foundation"
admin.site.index_title = "Key Education Foundation"

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Teacher_Query)
admin.site.register(Assesment)
