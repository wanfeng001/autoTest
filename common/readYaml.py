# pip install ruamel.yaml
# pip install pyyaml
import yaml
from ruamel import yaml
import os
file_data=os.path.join(os.getcwd(), "..\data\yamldata.yaml")

# 读取 yaml文件
def readYaml(file=file_data):
    with open(file,mode='r',encoding='utf-8') as f:
        cfg = f.read()
        yamlData = yaml.safe_load(cfg)
        return yamlData
# 写入 yaml文件
def writeYaml(file=file_data):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'A5RNW18316011440',
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'automationName': 'Uiautomator2',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
    with open(file,mode='w',encoding='utf-8') as f:
        yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)

y=readYaml()
print (y)