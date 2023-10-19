import gdown

# Set the Google Drive file ID
file_id = "1-bAHKckiWtvyYGe-D2wQbNNYnChqboL-"

# Set the output file path on your local system
output_file_path = "/workspaces/Ok/classpath.zip"

# Use gdown to download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file_path, quiet=False)