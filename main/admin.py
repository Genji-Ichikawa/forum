from django.contrib import admin

from main.models import Message, Topic

admin.site.register(Topic)
admin.site.register(Message)
