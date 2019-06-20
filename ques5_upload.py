# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'austin-2-pe'

# Gets bucket
bucket = storage_client.get_bucket(bucket_name)

blob = bucket.blob("austin.txt")

blob.upload_from_filename("austin.txt")
