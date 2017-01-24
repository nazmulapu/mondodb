import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.mdhasan
db.mdhasan.count()
mdhasan = db.mdhasan
mdhasan.find()



for bd1970 in range(2000):
    mdhasan = db.mdhasan.insert({"birthdate":"1970-01-01"});
print (bd1970)

for bd1985 in range(2000):
    mdhasan = db.mdhasan.insert({"birthdate":"1985-01-01"});
print(bd1985)

for bd1995 in range(2000):
    mdhasan = db.mdhasan.insert({"birthdate":"1995-01-01"});
print(bd1995)

for bd1980 in range(1800):
    mdhasan = db.mdhasan.insert({"birthdate":"1980-01-01"});
print(bd1980)

for name in range(100):
   mdhasan = db.mdhasan.insert({"name":"nazmul"});
print(name)

for fname in range(100):
   mdhasan = db.mdhasan.insert({"name":"Nazmul hasan"});
print(fname)


print (db.mdhasan.find({"birthdate":{"$lt":"1990-01-01"}}).count())
print (db.mdhasan.find({"birthdate":{"$gt":"1980-01-01"}}).count())
print (db.mdhasan.find({"name":"nazmul"}).count())
print (db.mdhasan.find({"name":{"$regex":"^nazmul"}}).count())

print(db.mdhasan.count())
