# Imports the Google Cloud client library
from google.cloud import storage
# Instantiates a client
storage_client = storage.Client()

bucket = storage_client.get_bucket("austin-1-pe")
blob = bucket.blob("hello.txt")

#deleting the file from source bucket
blob.delete()
print('Blob {} deleted.'.format("hello.txt"))
