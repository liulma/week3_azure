import os
import uuid

from azure.identity import DefaultAzureCredential

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

credential = DefaultAzureCredential()
print(f"Using credential: {credential.__class__.__name__}")
if hasattr(credential, 'credential'):  # Check for chained credential
    print(f"Chained credential: {credential.credential.__class__.__name__}")

# Retrieve the storage blob service URL, which is of the form
# https://<your-storage-account-name>.blob.core.windows.net/
storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]

# Create the client object using the storage URL and the credential
blob_client = BlobClient(
    storage_url,
    container_name="blob-container-01",
    blob_name=f"sample-blob-{str(uuid.uuid4())[0:5]}.txt",
    credential=credential,
)

# Open a local file and upload its contents to Blob Storage
with open("src\\data\\file_to_azure.txt", "rb") as data:
    blob_client.upload_blob(data)
    print(f"Uploaded file_to_azure.txt to {blob_client.url}")