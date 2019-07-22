import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.174.134:27017/")
mydb = myclient["ddsdb"]
mycol = mydb["t1"]

myquery = {"name": "Taobao"}

mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)