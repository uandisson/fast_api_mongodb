from datetime import date, datetime, time
from enum import Enum
from os import getenv
from typing import Dict, List

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from exceptions import mongodb_expection


def _transform_dict(dict_data: dict):
    def validation(v):
        if isinstance(v, date):
            return datetime.combine(v, time())
        if isinstance(v, list):
            return [validation(i) for i in v]
        if isinstance(v, dict):
            return _transform_dict(v)
        if isinstance(v, Enum):
            return v.value
        return v

    return {k: validation(v) for k, v in dict_data.items()}


def _get_db():
    mongodb_url = getenv("MONGODB_URL")
    client = MongoClient(mongodb_url)
    return client[getenv("MONGODB_DATABASE")]


class MongoDB:
    def __init__(self):
        self.db = _get_db()

    def save_document(self, collection: str, document: Dict) -> str:
        try:
            result = self.db[collection].insert_one(_transform_dict(document))
            return str(result.inserted_id)
        except DuplicateKeyError:
            raise mongodb_expection.DuplicateKeyError()

    def update_document(self, collection: str, key: Dict, document: Dict):
        result = self.db[collection].replace_one(key, _transform_dict(document))
        if result.matched_count == 0:
            raise mongodb_expection.DocumentNotFoundError(key)

    def get_by_filter(self, collection: str, key: Dict) -> List[Dict]:
        result = self.db[collection].find(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)

    def get_by_key(self, collection: str, key: Dict) -> Dict:
        result = self.db[collection].find_one(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)

    def delete_by_key(self, collection: str, key: Dict):
        result = self.db[collection].delete_one(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)
