import hashlib
from django.db import models

class Resume(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

    # File related fields
    file_hash = models.CharField(max_length=512, default='')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file:
            file_content = self.file.read()
            self.file_hash = hashlib.sha256(file_content).hexdigest()
            self.file.seek(0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
