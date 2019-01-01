from pymongo import MongoClient

client = MongoClient()
db = client.test

# insert
db.users.insert_one({"name": "Cristal P"})
db.userts.insert_many([{"name": "Holly"}, {"name": "Pete"}])

result = db.users.insert_one(
    {
        "name": "Bella",
        "address": {
            "street": "2 Avenue",
            "zip_code": "10075",
            "building": "1485"
        }
    }
)

# create consult
print("Insert and consult" + '\n')
cursor = db.users.find()

for document in cursor:
    print(document)

# Update
db.users.update_one({"name": "Cristal P"}, {"$set": {"name": "Cris P"}})

print("Update" + '\n')
cursor = db.users.find()
for document in cursor:
    print(document)

# Delete
result = db.users.delete_one({"name": "Cris P"})
print(result.deleted_count)

print("Delete" + "\n")
cursor = db.users.find()

for document in cursor:
    print(document)
