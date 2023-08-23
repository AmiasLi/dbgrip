from app.db.mongo.instance import MongoConnection


class MongoQuery(object):
    def __init__(self, host, port, db_name, username, password):
        self.connection = MongoConnection(host, port, db_name, username, password)
        self.connection.connect()

    def get_db(self):
        return self.connection.get_db()

    def get_collection(self, collection_name):
        return self.connection.get_collection(collection_name)

    def close(self):
        self.connection.close()
