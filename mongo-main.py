
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kumkum:kumkum@kumkum.t6aixbr.mongodb.net/?retryWrites=true&w=majority&appName=kumkum"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


mydb = client["kumkum"]
mycol = mydb["mycol"]
# mydict = { "name": "John", "address": "Highway 37" }

# Adds data in mycol variable
# x = mycol.insert_one(mydict)  


# Inserts dats in mycol named collection (here new mycol collection is made)
# mydb.mycol.insert_many([{"_id":"stu200", "name":"Ammu", "age":18},
#                        {"_id":"stu201", "name":"Priya", "age":29}])

# mydb.mycol.insert_one({"_id":"stu202", "name":"Kumkum", "age":18})
mydb.mycol.update_one({"age":19}, {"$set": {"age":22}})

# Prints the first data in mycol collection
# print(mycol.find_one())

# Prints all the data in mycol collection
# for x in mycol.find():
#     print(x)
    
