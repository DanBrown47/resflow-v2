from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'linkedin_url', 'github_url', 'file', 'uploaded_at', 'github_profile_json_path')
    search_fields = ('name', 'email', 'phone_number', 'address')
    list_filter = ('uploaded_at',)
    fields = ('name', 'email', 'phone_number', 'address', 'linkedin_url', 'github_url', 'file', 'uploaded_at', 'github_profile_json_path')
    readonly_fields = ('github_profile_json_path',)

    def github_profile_json_path(self, obj):
        return obj.github_profile_json_path()

    github_profile_json_path.short_description = 'GitHub Profile JSON Path'

admin.site.register(Resume, ResumeAdmin)
