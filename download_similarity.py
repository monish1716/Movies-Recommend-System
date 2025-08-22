import gdown

url = "https://drive.google.com/file/d/19jZMuhfHwXZrDr1XHH-2h0bKPXTkwoU_/view?usp=drive_link"
output = "similarity.pkl"
gdown.download(url, output, quiet=False)
