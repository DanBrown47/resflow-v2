import hashlib
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    file_hash = models.CharField(max_length=512, default='')  # Set default value
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
