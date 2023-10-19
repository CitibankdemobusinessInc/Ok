import gdown

# Replace the URL with your Google Drive file URL
url = 'https://drive.google.com/uc?id=1G29qEE56sCzhQ9Qpsbpk-vua0FOXj-Ih'

# Replace 'output_file' with the desired filename
output_file = 'your_file_name.extension'

gdown.download(url, output_file, quiet=False)