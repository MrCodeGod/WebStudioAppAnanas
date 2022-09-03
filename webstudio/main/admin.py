from django.contrib import admin
from .models import Content, User

admin.site.register(Content)
@admin .register(User)
class ContactAdmin(admin.ModelAdmin):
    pass
