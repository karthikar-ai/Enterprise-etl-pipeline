import boto3
import json


def upload_raw_data(data, bucket_name, file_name):
    s3 = boto3.client("s3")

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data),
        ContentType="application/json"
    )

    print(f"Raw data uploaded to S3: {file_name}")


def upload_json_file(file_path, bucket_name, s3_key):
    with open(file_path, "r") as file:
        data = json.load(file)

    upload_raw_data(data, bucket_name, s3_key)