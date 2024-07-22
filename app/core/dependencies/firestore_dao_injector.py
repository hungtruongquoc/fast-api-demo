from app.core.dao.firestore_dao import FirestoreDao
from app.services.firestore_client import db


def get_firestore_dao():
    return FirestoreDao(db)
