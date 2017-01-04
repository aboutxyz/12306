# coding:utf-8
import re
import pymongo
test=[]
'''
repls = ('hello', 'goodbye'), ('world', 'earth')
s = 'hello, world'
reduce(lambda a, kv: a.replace(*kv), repls, s)
'''
sname = []
connection = pymongo.MongoClient("localhost", 27017)
db = connection.train
collection = db.cityname
collection1 = db.stationname
collection2 = db.upstationname
for i in collection1.find():
    sname.append(i['name'])
for i in collection.find():
    i.setdefault('sub', 'none')
    i.setdefault('secsub', 'none')
    for j in sname:
        if any(x in j for x in [i['city'], i['sub'], i['secsub']]):
            print j,i
            i['station'] = j
            user = {"city": i['city'], "sub": i['sub'], "secsub": i['secsub'], "station": i['station']}
            collection2.insert(user)


