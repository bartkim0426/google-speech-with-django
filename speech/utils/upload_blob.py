from google.cloud import storage


def upload_blob(source_file_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client('speech-api')
    bucket = storage_client.get_bucket('speech-suwon')
    blob = bucket.blob(source_file_name)

    blob.upload_from_filename(source_file_name)
    blob.make_public()

    print('File {} uploaded to {}.'.format(
        source_file_name,
        source_file_name))
