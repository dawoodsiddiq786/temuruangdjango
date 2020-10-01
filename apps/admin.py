from django.contrib import admin

# Register your models here.
from apps.models import *

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Stay)
admin.site.register(Tour)

admin.site.register(Rating)
admin.site.register(Image)