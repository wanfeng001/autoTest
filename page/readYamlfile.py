import os
import yaml
from ruamel import yaml
base_url = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(base_url,'pageelement')
# 遍历读取yaml文件
def praseyaml():
    pageElement={}
    for fpath,dirname,fnames in os.walk(yamlpath):
        for name in fnames:
            yaml_path = os.path.join(fpath,name)
            if '.yaml' in str(yaml_path):
                with open(yaml_path,'r',encoding='utf-8') as f:
                    element = yaml.safe_load(f)
                    pageElement.update(element)
    return pageElement
y = praseyaml()
for i in y['HomePage']['locators']:
    print (i)
print (y['HomePage']['locators'][0])


