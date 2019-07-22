import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.174.134:27017/")
mydb = myclient["ddsdb"]
mycol = mydb["t1"]

#利用正则批量修改
myquery = {"name": {"$regex" : "^鸡" }}
newvalues = {"$set": {"name": "Github"}}

x = mycol.update_many(myquery, newvalues)

for line in mycol.find():
    print(line)