from urllib import request
import sys

myUrl = ""
myFile = ""

try:
    print("Start Downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("WARNING!!!")
    print(sys.exc_info())
    exit

print("File Downloaded and saved at: " + myFile)
