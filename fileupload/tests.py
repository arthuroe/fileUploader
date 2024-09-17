import boto3

from moto import mock_aws

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from django.conf import settings


@mock_aws
class FileUploadTests(APITestCase):

    
    def setUp(self):
        # Setup AWS mock S3 bucket
        self.s3 = boto3.client('s3', region_name='us-east-1')
        self.bucket_name = 'test-bucket'
        self.s3.create_bucket(Bucket=self.bucket_name)
        settings.AWS_STORAGE_BUCKET_NAME = self.bucket_name

    # @mock_aws
    def test_file_upload_encryption(self):
        # Create a test file
        file_data = b'Test content'
        uploaded_file = SimpleUploadedFile(
            'test.txt', file_data, content_type='text/plain')

        # Send POST request to upload and encrypt the file
        response = self.client.post(
            '/uploads/', {'file': uploaded_file}, format='multipart')

        # Assert the file was uploaded and encrypted successfully
        self.assertEqual(response.status_code, 201)
        self.assertIn('file_url', response.data)
        self.assertIn('encryption_key', response.data)

        # Check if the file exists in the mocked S3 bucket
        s3_objects = self.s3.list_objects_v2(Bucket=self.bucket_name)
        self.assertEqual(len(s3_objects['Contents']), 2)
