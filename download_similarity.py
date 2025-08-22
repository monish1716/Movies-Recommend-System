import gdown

url = "https://drive.google.com/uc?id=19jZMuhfHwXZrDr1XHH-2h0bKPXTkwoU_"
output = "similarity.pkl"
gdown.download(url, output, quiet=False)
