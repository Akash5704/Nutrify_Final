import gdown

# Replace with your Google Drive file ID
url = 'https://drive.google.com/file/d/1FkFoP9ZYuRsi2HWdCfcK686vawXG6eFb/view?usp=drivesdk'
output = 'dataset.zip'
gdown.download(url, output, quiet=False)
