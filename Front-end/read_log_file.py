import json
from os import path
from matplotlib.pyplot import get

def refesh_result():
    with open('response.json') as datafile:
        datastore = json.load(datafile)

    #------> for get all element in json file
    # [print(ele['File name']) for ele in datastore ]

    lastest = datastore[-1]
    # label_Name = lastest['Name']
    # label_Percent = lastest['Percent']
    # label_Date_Time = lastest['Time']
    return lastest
# print("Name :",label_Name)
# print("Percent :",label_Percent)
# print("Date time :",label_Date_Time)
# print("result :",label_predict[0],label_predict[1])
# print("Date :",label_Date_Time[0])
# print("Time :",label_Date_Time[1])

def getDate(label_Date_Time): return label_Date_Time.split(" ")[0]
def getTime(label_Date_Time): return label_Date_Time.split(" ")[1]
def getName(label_Name): return label_Name
def getResultPrecent(label_Percent): return label_Percent

def find_most_acc(label_Name,label_Percent,p_result):
    re = label_Percent[p_result]
    if int(re) >= 80 :
        return label_Name[p_result], label_Percent[p_result]
    else :
        return "Unknown", 0

def find_most_acc_percent(label_Percent,p_result):
    return 

# print(getDate())
# print(getTime())
# print(getName())
# print(getResultPrecent())

def most_3_people(arr_response):
    arr_name = arr_response['Name']
    arr_percent = arr_response['Percent']
    for i in range(len(arr_name)):
        for j in range(0, len(arr_percent)-i-1):
            if arr_percent[j] < arr_percent[j+1]:
                arr_percent[j], arr_percent[j+1] = arr_percent[j+1], arr_percent[j]
                arr_name[j], arr_name[j+1] = arr_name[j+1], arr_name[j]
    
    return_name = arr_name[0:3]  
    return_percent = arr_percent[0:3]        
    return return_name, return_percent
    
def write_time(now,fname):
    filename = 'time_process.json'
    if path.isfile(filename) is False:
      raise Exception("File not found")

    # # Read JSON file
    with open(filename) as fp:
      listObj = json.load(fp)
    
    last = {}
    last['Processing_Time'] = now
    last['filename'] = str(fname)
    print(last)
    print(type(last))
    
    listObj.append(last)
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
        
        
        
def refresh_pin_status():
    with open('status.json') as datafile:
        status_file = json.load(datafile)
        
    return status_file["message"]