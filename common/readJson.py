import os
import json
from common import configpath

file_data = configpath.json_path

class ReadJson:
    def __init__(self):
        self.file_data = file_data

    # 读取json文件
    def getToken(self):
        file = self.file_data
        with open(file, mode='r') as f:
            jsonData = f.read()
            dictData = json.loads(jsonData)
            return dictData['token']

    # 写入json文件
    def writeToken(self, *args):
        file = self.file_data
        with open(file, mode='w') as f:
            dictData = {"token": args[0], "newToken": args[1]}  # 加‘，’可以多个值写入
            jsonData = json.dumps(dictData)
            f.write(jsonData)
            return jsonData


if __name__ == '__main__':
    j = ReadJson()
    rt = j.getToken()
    print(rt)
    wt = j.writeToken(1,2)
    print(wt)
