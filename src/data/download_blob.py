import io
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient

def download_blob_to_file(blob_service_client: BlobServiceClient, container_name: str): # Removed self
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample-blob-dac97.txt")
    with open(file=os.path.join(r'src\\data', 'file_from_azure.txt'), mode="wb") as sample_blob:
        download_stream = blob_client.download_blob()
        sample_blob.write(download_stream.readall())

if __name__ == "__main__":
    # Replace with your storage account URL
    account_url = "https://lindasdkdemo.blob.core.windows.net"
    credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    # Specify the container name
    container_name = "blob-container-01"
    download_blob_to_file(blob_service_client, container_name)