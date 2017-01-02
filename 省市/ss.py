#coding:utf-8
import json
import re
import requests

with open('js.json','r')as f:
    for i in f:
        data = json.loads(i.decode('gbk').encode('utf-8'))
        for j in data:
            if j['name'] in [u"请选择",u"其他",u"海外"]:
                pass
            else:
                print j['name']
            try:
                for x in j['sub']:
                    if x['name'] in [u"请选择",u"其他"]:
                        pass
                    else:
                        print x['name']
            except KeyError:
                pass
                