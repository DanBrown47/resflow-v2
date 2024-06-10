from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Resume

class FileExtensionValidator:
    allowed_extensions = ['pdf', 'txt', 'docx']

    def __call__(self, value):
        extension = value.name.split('.')[-1].lower()
        if extension not in self.allowed_extensions:
            raise ValidationError(
                _('File type %(extension)s is not supported. Only PDF, TXT, and DOCX files are allowed.'),
                params={'extension': extension},
            )

class ResumeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    file = serializers.FileField(validators=[FileExtensionValidator()])

    class Meta:
        model = Resume
        fields = ['id', 'name', 'email', 'file', 'uploaded_at']
