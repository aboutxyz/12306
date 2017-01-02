#coding:utf-8
import json
import pymongo

with open('js.json', 'r')as f:
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection.train
    collection = db.cityname
    for i in f:
        data = json.loads(i.decode('gbk').encode('utf-8'))
        for j in data:
            if j['name'] not in [u"请选择", u"其他", u"海外"]:
                for x in j['sub']:
                    if x['name'] not in [u"请选择", u"其他"]:
                        try:
                            for z in x['sub']:
                                if z['name'] not in [u"请选择", u"其他"]:
                                    collection.insert({"city": j['name'], "sub": x['name'], "secsub": z['name']})
                        except KeyError:
                            collection.insert({"city": j['name'], "sub": x['name']})
