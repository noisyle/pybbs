from django.contrib import admin
from bbs.models import Thread,Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Thread)
