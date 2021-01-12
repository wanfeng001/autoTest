# pip install ruamel.yaml
# pip install pyyaml
import yaml
from ruamel import yaml
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_data = os.path.join(ROOT_DIR,'data\yamldata.yaml')


class ReadYaml:
    def __init__(self):
        self.file_data = file_data

    # 读取 yaml文件
    def readYaml(self):
        file = self.file_data
        with open(file,mode='r',encoding='utf-8') as f:
            cfg = f.read()
            yamlData = yaml.safe_load(cfg)
            return yamlData['desired_caps']

    # 写入 yaml文件
    def writeYaml(self):
        file = self.file_data
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'A5RNW18316011440',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'automationName': 'UiAutomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }
        with open(file,mode='w',encoding='utf-8') as f:
            yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)

if __name__ == '__main__':
    y = ReadYaml()
    yamldata = y.readYaml()
    print(yamldata)