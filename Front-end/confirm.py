import requests
import json

url = "http://10.98.6.65:5000/confirm"
file = "status.json"

def YES(name):
    payload = json.dumps({ "status": "YES","name": name})
    headers = {'Content-Type': 'application/json' }
    response = requests.request("POST", url, headers=headers, data=payload)


def NO(code):
    url = "http://10.98.6.65:5000/confirm"

    payload = {
        "status" : "NO",
        "code" : code
    }

    headers = {"Content-Type":"application/json"}

    response = requests.request("POST",url,json=payload,headers=headers)
    
    print(response.json())
    
    with open(file, "w") as ff :
        ff.write(json.dumps(response.json()))

def Nothing():
    payload = json.dumps({ "status": "IDLE"})
    headers = {'Content-Type': 'application/json' }
    response = requests.request("POST", url, headers=headers, data=payload)

# YES()
# NO()