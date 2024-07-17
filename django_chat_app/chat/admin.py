from django.contrib import admin
from .models import Chat,Message

class AuthorAdmin(admin.ModelAdmin):
    fields = ('chat','text','created_at','author','receiver')
    list_display = ('chat','text','created_at','author','receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, AuthorAdmin)
admin.site.register(Chat)
