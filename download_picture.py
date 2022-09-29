from urllib import request
import sys

myUrl = "https://becloud.by/upload/medialibrary/99d/yxqpovo4n4spgidn6y19j1zvpc0j6hju/obl_Storage.png"
myFile = "C:\Users\sergey.buhtiyarov\Pictures\mykartinka.jpg"

try:
    print("Start Downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("WARNING!!!")
    print(sys.exc_info())
    exit

print("File Downloaded and saved at: " + myFile)
