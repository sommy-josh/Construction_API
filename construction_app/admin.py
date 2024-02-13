from django.contrib import admin

# Register your models here.
from .models import Contact,Home,GetQUote

admin.site.register(Home),
admin.site.register(GetQUote),
admin.site.register(Contact),