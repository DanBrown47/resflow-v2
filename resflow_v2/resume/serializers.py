from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Resume
import re

class FileExtensionValidator:
    allowed_extensions = ['pdf', 'docx']

    def __call__(self, value):
        extension = value.name.split('.')[-1].lower()
        if extension not in self.allowed_extensions:
            raise ValidationError(
                f'File type {extension} is not supported. Only PDF and DOCX files are allowed.'
            )

class ResumeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    file = serializers.FileField(validators=[FileExtensionValidator()])

    def validate_phone_number(self, value):
        # Validate phone number format
        if not re.match(r'^\+?\d{10,}$', value):  # Adjust regex as needed
            raise serializers.ValidationError('Invalid phone number format. Must be in the format +XXXXXXXXXX or XXXXXXXXXX.')
        return value

    def validate_linkedin_url(self, value):
        # No validation needed, so simply return the value
        return value

    class Meta:
        model = Resume
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'linkedin_url', 'website_url', 'file', 'uploaded_at']

    def validate(self, data):
        # Call superclass' validate to ensure all default validations are done
        super().validate(data)

        # Validate phone_number if present in data
        phone_number = data.get('phone_number')
        if phone_number:
            self.validate_phone_number(phone_number)

        return data
