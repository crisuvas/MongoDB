from pymongo import MongoClient

client = MongoClient()
db = client.test

# clean the data
db.cars.delete_many({})
db.pilots.delete_many({})

# insert
db.cars.insert_one({"model": "tsuru", "license": "435-mdgf", "id_pilot": 1})
db.cars.insert_one({"model": "mazda", "license": "328-shes", "id_pilot": 2})
db.cars.insert_one({"model": "beetle", "license": "928-dash", "id_pilot": 3})
db.pilots.insert_many([{"id_pilot": 1, "name": "George", "age": 32},
                       {"id_pilot": 2, "name": "Georgia", "age": 54},
                       {"id_pilot": 3, "name": "Cristi", "age": 25}])

# select
print("Select" + '\n')
cursor = db.pilots.find()
cursor_2 = db.cars.find()

for pilot in cursor:
    print(pilot)

for car in cursor_2:
    print(car)

# Update
db.cars.update_one({"model": "tsuru"}, {"$set": {"model": "Audi"}})

print("Update" + '\n')
cursor = db.cars.find()
for car in cursor:
    print(car)

# Delete
result = db.cars.delete_one({"model": "beetle"})
print(result.deleted_count)

print("Delete" + "\n")
cursor = db.cars.find()

for car in cursor:
    print(car)
