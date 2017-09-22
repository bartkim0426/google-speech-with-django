from google.cloud import storage


def download_blob(source_blob_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client('speech-api')
    bucket = storage_client.get_bucket('speech-suwon')
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(source_blob_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name, source_blob_name))
