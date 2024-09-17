import boto3

from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_file(file_path, key):
    """
    Function to encrypt file
    """
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    encrypted_path = f"{file_path}.encrypted"
    with open(encrypted_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return encrypted_path


def upload_to_s3(file_path, file_name, bucket_name):
    """
    Function to upload file to s3 bucket
    """
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, file_name)
    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
