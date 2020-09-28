from django.contrib import admin

# Register your models here.
from apps.models import User, Activity, Image

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Image)