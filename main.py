# coding:utf-8
import re
import pymongo
test=[]
with open('stationname.js','r') as f:
    # patten = re.compile(r"@([a-z]*)\|([\x80-\xff]*)\|([A-Z]*)\|([a-z]*)\|([a-z]*)\|([0-9]*)")
    patten = re.compile(r"@([a-z]*)\|(.*?)\|([A-Z]*)\|([a-z]*)\|([a-z]*)\|([0-9]*)")
    resu= f.read()
    result = patten.findall(resu)
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection.train
    collection = db.stationname
    for i in result:
        user = {"name": i[1].decode('gbk'), "code": i[2]}
        collection.insert(user)
