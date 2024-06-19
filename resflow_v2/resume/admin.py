from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'linkedin_url', 'website_url', 'file', 'uploaded_at')
    search_fields = ('name', 'email', 'phone_number', 'address')
    list_filter = ('uploaded_at',)

    fields = ('name', 'email', 'phone_number', 'address', 'linkedin_url', 'website_url', 'file', 'cover_letter_text', 'cover_letter_file', 'uploaded_at')

admin.site.register(Resume, ResumeAdmin)
