from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kumkum:kumkum@kumkum.t6aixbr.mongodb.net/?retryWrites=true&w=majority&appName=kumkum"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["kumkum"]
mycol = mydb["mycol"]

# Uncomment to insert data
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)

# Uncomment to update data
# mydb.mycol.update_one({"age":19}, {"$set": {"age":22}})

# Uncomment to retrieve and print all data
# for x in mycol.find():
#     print(x)
