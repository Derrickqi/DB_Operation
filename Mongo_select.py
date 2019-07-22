import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.174.134:27017/")
mydb = myclient["ddsdb"]
mycol = mydb["t1"]

for x in mycol.find():
    print(x)