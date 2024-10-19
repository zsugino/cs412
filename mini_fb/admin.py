# File: admin.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: registers profile model to the admin interface

from django.contrib import admin

from .models import Profile, StatusMessage, Image
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)