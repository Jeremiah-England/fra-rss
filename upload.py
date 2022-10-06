import os
import json
import boto3


aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

if not aws_access_key_id or not aws_secret_access_key:
    with open("./secrets.json") as f:
        secrets = json.load(f)
        aws_access_key_id = secrets["github-fra-rss"]
        aws_secret_access_key = secrets["secret"]

session = boto3.session.Session()
client = session.client(
    "s3",
    endpoint_url="https://nyc3.digitaloceanspaces.com",
    region_name="nyc3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

directory = "generated"
for file in os.listdir(directory):
    print(f"Uploading '{directory}/{file}'")

    with open(f"{directory}/{file}", "r") as f:
        contents = f.read()

    client.put_object(
        Bucket="fra-rss",
        Key=file,
        Body=contents,
        ACL="public-read",
    )
