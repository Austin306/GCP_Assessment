# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()
source_bucket = storage_client.get_bucket("austin-1-pe")
source_blob = source_bucket.blob("hi.txt")
destination_bucket = storage_client.get_bucket("austin-2-pe")
new_blob = source_bucket.copy_blob(
source_blob, destination_bucket, "copy_hi.txt")
print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
source_blob.name, source_bucket.name, new_blob.name,
destination_bucket.name))
