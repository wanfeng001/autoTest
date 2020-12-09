import os
import json
file_data=os.path.join(os.getcwd(), "..\data\jsondata.json")
def getToken(file=file_data):
    with open(file,mode='r') as f:
        jsonData=f.read()
        dictData = json.loads(jsonData)
        print(type(dictData))
        return  dictData['token']

dictData = json.load(open(file_data,mode='r'))
print (dictData)
print (getToken())

token='12345'
newToken = '56789'
def writeToken(*tokenValue):
    with open(file=file_data,mode='w') as f:
        dictData ={"token":tokenValue[0],"newToken":tokenValue[1]} # 加‘，’可以多个值写入
        print(type(dictData))
        jsonData =json.dumps(dictData)
        print(type(jsonData))
        f.write(jsonData)

writeToken(token,newToken)
