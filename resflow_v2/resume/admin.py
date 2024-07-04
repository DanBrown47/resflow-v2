from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'linkedin_url',  'github_url', 'file', 'uploaded_at')
    search_fields = ('name', 'email', 'phone_number', 'address')
    list_filter = ('uploaded_at',)
    readonly_fields = ('uploaded_at', 'file_hash')
    fields = ('name', 'email', 'phone_number', 'address', 'linkedin_url',  'github_url', 'file')

admin.site.register(Resume, ResumeAdmin)
