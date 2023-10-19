import gdown

# Set the Google Drive file ID.
file_id = '18EMPgqYMvHwbRFpgiRNb8ePPnCuB2ABj'

# Set the output file path in your Colab environment.
output_file_path = '/content/my-downloaded-file.txt'

# Use gdown to download the file.
gdown.download(f'https://drive.google.com/uc?id={file_id}', output_file_path, quiet=False)