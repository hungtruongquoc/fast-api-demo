class FirestoreDao:
    def __init__(self, db):
        self.db = db

    def get_all(self, collection):
        return self.db.collection(collection).get()

    def get(self, collection, document_id: str):
        return self.db.collection(collection).document(document_id).get()

    def create(self, collection, data):
        return self.db.collection(collection).add(data)

    def update(self, collection, document_id, data):
        return self.db.collection(collection).document(document_id).update(data)

    def delete(self, collection, document_id):
        return self.db.collection(collection).document(document_id).delete()
