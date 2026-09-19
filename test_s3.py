from s3_uploader import upload_raw_data

data = {
    "customer_id": "C001",
    "name": "Test User",
    "email": "test@example.com"
}

print("Raw JSON data prepared for S3 upload.")
print("Data:", data)