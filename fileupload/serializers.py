from rest_framework import serializers

from .models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['file', 'encrypted_file_path', 'uploaded_at']
        