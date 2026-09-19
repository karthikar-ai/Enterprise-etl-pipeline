import boto3
from moto import mock_aws
from s3_uploader import upload_json_file


@mock_aws
def test_s3_upload():
    s3 = boto3.client("s3", region_name="us-east-1")

    bucket_name = "test-etl-bucket"
    s3.create_bucket(Bucket=bucket_name)

    upload_json_file(
        "raw_data/stripe_customers.json",
        bucket_name,
        "raw/stripe_customers.json"
    )

    response = s3.get_object(
        Bucket=bucket_name,
        Key="raw/stripe_customers.json"
    )

    print("S3 mock upload successful.")
    print(response["Body"].read().decode())


test_s3_upload()