import pymongo

class Server:
    def __init__(self, database_name= "Ambivolt", url= 'mongodb+srv://straga:zeus16hades@maincluster-aybxn.mongodb.net/test?retryWrites=true&w=majority'):

        self.client = pymongo.MongoClient(url)
        self.databaseList = self.client.list_database_names()

        self.database =  None
        self.create_database(database_name)

        self.collectionList = self.database.list_collection_names()
        self.collection = []

    def create_database(self, database_name):
        self.database = self.client[database_name]
        if database_name not in self.databaseList:
            self.create_collection("dummy")

    def create_collection(self, name):
        if name not in self.collectionList:
            self.collection.append(self.database[name])
            self.collection[0].insert_one({})

    def insert_one_in_collection(self, name, dict):
        return self.database[name].insert_one(dict).inserted_id

    def insert_multiple_in_collection(self, name, list):

        for dict in list:
            self.insert_one_in_collection(name, dict)

#mycol = mydb["customers"] # creates new collection
#mydict = { "name": "Bogdan", "address": "eu da eu" }
#x = mycol.insert_one(mydict) # creates new entry
#print(x.inserted_id)

mycol.delete_many({})# delete data grom collection

"""""
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
"""""

""""
{ "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
"""

#x = mycol.insert_many(mylist)

for x in mycol.find({},{ "_id": 0, "name": "John", "address": 1 }):
  print(x)

# ids = x.inserted_ids
#
# print(id)
#
# dblist  = myclient.list_database_names()
#
# collist = mydb.list_collection_names()
# for elem in collist:
#   print(elem)

#for elem in readCollection:
#  print(elem)

#for elem in dblist:
#  print(elem)

#if "mydatabase" in dblist:
#  print("The database exists.")