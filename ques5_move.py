# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

#copying the file
source_bucket = storage_client.get_bucket("austin-2-pe")
source_blob = source_bucket.blob("copy_hi.txt")
destination_bucket = storage_client.get_bucket("austin-1-pe")
new_blob = source_bucket.copy_blob(
source_blob, destination_bucket, "hello.txt")
print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
source_blob.name, source_bucket.name, new_blob.name,
destination_bucket.name))

#deleting the file from source bucket
source_blob.delete()
print('Blob {} deleted.'.format("copy_hi.txt"))
