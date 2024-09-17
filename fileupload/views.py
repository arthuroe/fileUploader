from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import FileUpload
from .serializers import FileUploadSerializer
from .utils import generate_key, encrypt_file, upload_to_s3


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):
        file_serializer = self.get_serializer(data=request.data)

        if file_serializer.is_valid():
            # Save the original file
            file_instance = file_serializer.save()

            # Encrypt the file
            key = generate_key()
            encrypted_file_path = encrypt_file(file_instance.file.path, key)

            # Save the encrypted file to S3 or local storage
            if settings.USE_S3:
                file_url = upload_to_s3(
                    encrypted_file_path, file_instance.file.name,
                    settings.AWS_STORAGE_BUCKET_NAME
                )
            else:
                file_url = encrypted_file_path

            # Update file instance with encrypted path
            file_instance.encrypted_file_path = file_url
            file_instance.save()

            return Response({
                'file_url': file_url,
                'encryption_key': key.decode()
            }, status=status.HTTP_201_CREATED)

        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
