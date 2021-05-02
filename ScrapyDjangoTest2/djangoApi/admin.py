from django.contrib import admin
from .models import Match

class MovieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Match, MovieAdmin)