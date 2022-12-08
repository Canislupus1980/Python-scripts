# GET-request

from urllib import request

myUrl = ""

answer = request.urlopen(myUrl)
mytext1 = answer.realines()
mytext2 = answer.read()

print(answer)
print(mytext2)

for line in mytext1:
     print(line)

# POST-request

from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"
value = {'q': ''}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'


try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    reply = request.urlopen(req)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:        
        print("Error occuried during web request!!")
        print(sys.exc_info()[1])
