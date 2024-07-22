from app.core.dao.firestore_dao import FirestoreDao


class FirestoreService:
    def __init__(self, dao: FirestoreDao):
        self.dao = dao

    def get_scheduling_rules(self):
        return self.dao.get_all("scheduling_rules")
