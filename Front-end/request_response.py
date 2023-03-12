import json
from os import path
import requests

url = "http://10.98.6.65:5000/file-upload"
filename = 'response.json'

def sendImg(sendFile):
  try:
    listObj = []
    payload={}
    files = [('file', (f'{sendFile}', open(f'./{sendFile}', 'rb'), 'image/jpeg'))]
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