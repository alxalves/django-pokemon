from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Pokemon, Move, Ribbon

# Register your models here
admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(Ribbon)
