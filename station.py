# coding:utf-8
import re
import pymongo
test=[]
'''
repls = ('hello', 'goodbye'), ('world', 'earth')
s = 'hello, world'
reduce(lambda a, kv: a.replace(*kv), repls, s)
'''
stationlist = []
with open('stationname.js','r') as f:
    patten = re.compile(r"@([a-z]*)\|(.*?)\|([A-Z]*)\|([a-z]*)\|([a-z]*)\|([0-9]*)")
    resu= f.read()
    result = patten.findall(resu)
    # connection = pymongo.MongoClient("localhost", 27017)
    # db = connection.train
    # collection = db.station
    for i in result:
        repls = (u'东', '',1), (u'南', '',1), (u'西', '',1), (u'北', '',1)
        x = i[1].decode('gbk')[:-1] + reduce(lambda a, kv: a.replace(*kv), repls, i[1].decode('gbk')[-1])
        stationlist.append(x)
    for i in stationlist:
        print i
        # if i[1].decode('gbk')
        # user = {"name": i[1].decode('gbk'), "code": i[2]}
        # collection.insert(user)
