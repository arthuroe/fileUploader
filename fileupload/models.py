from django.db import models


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    encrypted_file_path = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
