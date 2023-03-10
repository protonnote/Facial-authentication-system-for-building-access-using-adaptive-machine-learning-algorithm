import json
from os import path
from matplotlib.pyplot import flag
import requests

url = "http://10.98.6.65:5000/file-upload"
filename = 'response.json'

def sendImg(sendFile) :
  try :
    listObj = []
    payload={}
    files = [('file',('{}'.format(sendFile),open('./{}'.format(sendFile),'rb'),'image/jpeg'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    # # Check if file exists
    if path.isfile(filename) is False:
      raise Exception("File not found")

    # # Read JSON file
    with open(filename) as fp:
      listObj = json.load(fp)
    
    listObj.append(response.json())
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    return True
  except :
    return False


# files = {'f': ('1.pdf', open('1.pdf', 'rb'))}
# response = requests.post("https://pdftables.com/api?&format=xlsx-single",files=files)
# response.raise_for_status() # ensure we notice bad responses
# response = requests.get("http://localhost:5000/")
# with open("response.text", "wb") as f:
#     f.write(response.content)
# print('Successfully appended to the JSON file')


# sendImg("ttest.jpg")
# sendImg("some-one.jpg")