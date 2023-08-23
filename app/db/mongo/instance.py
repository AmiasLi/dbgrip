import pymongo


class MongoConnection(object):
    def __init__(self, host, port, db_name, username, password):
        self.db = None
        self.client = None
        self.host = host
        self.port = port
        self.db_name = db_name
        self.username = username
        self.password = password

    def connect(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]
        self.db.authenticate(self.username, self.password)

    def get_db(self):
        return self.db

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()
