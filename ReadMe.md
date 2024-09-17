# Django DRF File Upload API to AWS S3

This project provides an API for uploading files, encrypting them, and storing them either in AWS S3 or locally.

## Setup

1. Clone the repository:

   ```bash
   git clone <repo_url>
   cd fileupload_project
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure AWS settings in `.env` and other environment variables.
   Use `.env.example`.

   ```bash
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_STORAGE_BUCKET_NAME=your_bucket_name
   AWS_S3_REGION_NAME=your_aws_region
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create superuser(Optional):

   ```bash
   python manage.py createsuperuser
   ```

7. Start development server:

   ```bash
   python manage.py runserver
   ```

8. How to test:

   ```
   curl -X POST -F 'file=@/<path to file>' http://127.0.0.1:8000/uploads/
   ```

   Test with Postman:

   ```
    - Open Postman and set the request type to POST.
    - Set the URL to http://127.0.0.1:8000/uploads/.
    - In the "Body" tab, select "form-data".
    - Add a key named file and set its type to "File".
    - Choose a file to upload.
    - Click "Send" to perform the upload.
   ```

9. Run tests:
   ```bash
   python manage.py test
   ```
