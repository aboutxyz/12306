# coding:utf-8
import re
import pymongo
test=[]
'''
repls = ('hello', 'goodbye'), ('world', 'earth')
s = 'hello, world'
reduce(lambda a, kv: a.replace(*kv), repls, s)
repls = (u'东', ''), (u'南', ''), (u'西', ''), (u'北', '')
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
    stationlist = []
    i.setdefault('sub', 'none')
    i.setdefault('secsub', 'none')
    for j in sname:# sname 是站名
        if any(x.replace(u'县', '').startswith(j) for x in [i['city'], i['sub'], i['secsub']]):
            print j,i
            stationlist.append(j)
            for y in sname[:]:
                if j in y:
                    stationlist.append(y)
    user = {"city": i['city'], "sub": i['sub'], "secsub": i['secsub'], "station": list(set(stationlist))}
    collection2.insert(user)


