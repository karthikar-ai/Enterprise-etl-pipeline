from s3_uploader import upload_raw_data

data = {
    "customer_id": "C001",
    "name": "Test User",
    "email": "test@example.com"
}

# S3 upload will be tested when AWS credentials are available.
print("Raw JSON data prepared for S3 upload.")