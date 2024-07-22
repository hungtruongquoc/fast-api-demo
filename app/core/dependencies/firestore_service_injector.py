from fastapi import Depends

from app.core.dao.firestore_dao import FirestoreDao
from app.core.dependencies.firestore_dao_injector import get_firestore_dao
from app.core.services.firestore_service import FirestoreService


def get_firestore_service(dao: FirestoreDao = Depends(get_firestore_dao)) -> FirestoreService:
    return FirestoreService(dao)
