from django.contrib import admin

from .models import Voter, Flag, Vote 

admin.site.register(Voter)
admin.site.register(Flag)
admin.site.register(Vote)
