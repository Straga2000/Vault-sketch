import pymongo

class Database:
    def __init__(self,url, database_name= "Ambivolt"):

        self.client = pymongo.MongoClient(url)
        print ("Initializam clientul")
        self.database = None
        self.databaseList = None
        self.collectionList = None

        self.refresh_database_list()

        self.create_database(database_name)
        self.refresh_collection_list()



    def refresh_database_list(self):
        self.databaseList = self.client.list_database_names()

    def refresh_collection_list(self):
        self.collectionList = self.database.list_collection_names()

    def create_database(self, database_name):
        self.database = self.client[database_name]
        if database_name not in self.databaseList:
            self.refresh_database_list()
            self.create_collection("dummy")

    def create_collection(self, name):
        if self.collectionList is None or name not in self.collectionList:
            self.refresh_collection_list()
            self.database[name].insert_one({"type" : "dummmy"})

    def insert_one_in_collection(self, name, dict):
        return self.database[name].insert_one(dict)

    def insert_multiple_in_collection(self, name, list):
        return self.database[name].insert_many(list)

    def delete_collection(self, name):
        self.database[name].drop()
        self.refresh_collection_list()

    def delete_insertion(self, name, dict):
        self.database[name].delete_one(dict)

    def delete_multiple_insertion(self, name, list):
        self.database[name].delete_many(list)

    def print_collection(self, name):
        for x in self.database[name].find():
            print (x)

    def query_many(self, name, query= None):
        if query is None:
            return self.database[name].find({"_id: 0"})
        else:
            return self.database[name].find({"_id : 0"}, query)

    def query_one(self, name, query= None):
        if query is None:
            return self.database[name].find()
        else:
            return self.database[name].find({}, query)

    def count(self, name, query= None):
        if query is None:
            return self.database[name].count_documents()
        else:
            return self.database[name].count_documents(query)

db = Database('yes')

obj = {"age" : "12"}

#db.insert_one_in_collection("dummy", obj)
db.print_collection("dummy")
#db.delete_collection("dummy")