from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Player_history)
admin.site.register(Match)
admin.site.register(Points)