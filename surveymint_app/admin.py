from django.contrib import admin
from .models import researcher, participant, interview

# Register your models here.

admin.site.register(researcher)
admin.site.register(participant)
admin.site.register(interview)