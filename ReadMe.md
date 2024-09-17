# Django DRF File Upload API with ViewSets, Encryption, and AWS S3

This project provides an API for uploading files, encrypting them, and storing them either in AWS S3 or locally.

## Setup

1. Clone the repository:

   ```bash
   git clone <repo_url>
   cd fileupload_project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS settings in .env and other environment variables
   Use .env.example

   ```bash
   USE_S3="True or False"
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_STORAGE_BUCKET_NAME=your_bucket_name
   AWS_S3_REGION_NAME=your_aws_region
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create superuser(Optional):

   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:

   ```bash
   python manage.py runserver
   ```

7. How to test:

   ```
   curl -X POST -F 'file=@/<path to file>' http://127.0.0.1:8000/uploads/
   ```

8. Run tests:
   ```bash
   python manage.py test
   ```
