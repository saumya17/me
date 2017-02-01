from pymongo import MongoClient
client = MongoClient()

def findThreeVacantSlots():
    count = 0
    letVacant = 100
    available = []
    while count != 3:
        if db.Permissions.find({"permissions.permission_id": letVacant}).count() == 0:
            count += 1
            available.append(letVacant)
            letVacant += 1
    return available

client = MongoClient()
db = client.core
collection = db.Permissions

availableID = findVacant()

db.Permissions.insertOne({"display_name":"DQT Access","name":"dqt_access","priority":18,"permissions":[{"name":"dqt.can_create","permission_id":availableID[1],"display_name":"Can create DQT"},{"name":"dqt.can_view","permission_id":availableID[2],"display_name":"Can view DQT"}]})
db.Permissions.update({"name":"menu"},{ $push: { "permissions": {"name":"menu.can_dqt","permission_id":availableID[0],"display_name":"Can View Quality"}}})
