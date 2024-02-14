from django.contrib import admin

# Register your models here.
from .models import Contact,Home,GetQUote

admin.site.header('Construction Admin')
class HomeAdmin(admin.ModelAdmin):
    inlines = ['text','image']

admin.site.register(Home,HomeAdmin),
admin.site.register(GetQUote),
admin.site.register(Contact),