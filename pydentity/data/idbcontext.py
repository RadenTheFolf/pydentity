from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from ientry import IEntry
from pydentity.force_super import ForceBaseCallMeta, force_super_call
from cache import Cache
from change_tracker import ChangeTracker
from idatabase import IDatabase


class IDbContext(metaclass=ForceBaseCallMeta):
    Database: IDatabase = None
    Cache: Cache = None
    ChangeTracker: ChangeTracker = None

    def __init__(self, database, db_name: str):
        if not issubclass(database, IDatabase):
            raise TypeError("Database must be a subclass of IDatabase")
        self.Database = database(db_name)
        self.Cache = Cache()
        self.ChangeTracker = ChangeTracker({})

    @abstractmethod
    @force_super_call
    def save_changes(self):
        self.ChangeTracker.clear_changes()


    @abstractmethod
    @force_super_call
    async def save_changes_async(self):
        self.ChangeTracker.clear_changes()

    @abstractmethod
    @force_super_call
    def rollback(self):
        old_data = self.ChangeTracker.get_original_data()
        change_data = self.ChangeTracker.get_changes()
        self.ChangeTracker.set_data(old_data)
        self.ChangeTracker.clear_changes()
        seen = []
        for k, v in change_data:
            if k not in seen:
                seen.append(k)
                self.Cache[k] = v

    @abstractmethod
    @force_super_call
    def insert(self, key, value):
        self.Cache[key] = value
        self.ChangeTracker[key] = value

    @abstractmethod
    @force_super_call
    def insert_object(self, obj: IEntry):
        self.Cache[obj.get_id()] = obj.to_dict()
        self.ChangeTracker[obj.get_id()] = obj.to_dict()

    @abstractmethod
    @force_super_call
    def insert_many(self, data: list):
        for k, v in data:
            self.Cache[k] = v
            self.ChangeTracker[k] = v

    @abstractmethod
    @force_super_call
    def insert_many_objects(self, data: list):
        for obj in data:
            self.Cache[obj.get_id()] = obj.to_dict()
            self.ChangeTracker[obj.get_id()] = obj.to_dict()

    @abstractmethod
    @force_super_call
    def get(self, key):
        if self.Cache.has_key(key):
            return self.Cache[key]
        else:
            return None

    @abstractmethod
    @force_super_call
    def get_object(self, obj: IEntry):
        if self.Cache.has_key(obj.get_id()):
            obj.from_dict(self.Cache[obj.get_id()])
            return obj
        else:
            return None

    @abstractmethod
    @force_super_call
    def delete(self, key):
        if self.Cache.has_key(key):
            del self.Cache[key]
            del self.ChangeTracker[key]

    @abstractmethod
    @force_super_call
    def delete_object(self, obj: IEntry):
        if self.Cache.has_key(obj.get_id()):
            del self.Cache[obj.get_id()]
            del self.ChangeTracker[obj.get_id()]

    @abstractmethod
    @force_super_call
    def has_key(self, key):
        return self.Cache.has_key(key)

    @abstractmethod
    @force_super_call
    def has_object(self, obj: IEntry):
        return self.Cache.has_key(obj.get_id())

    @abstractmethod
    @force_super_call
    def find_by(self, key, value):
        for k, v in self.Cache.get_items():
            if v[key] == value:
                return v
        else:
            return None

    @abstractmethod
    @force_super_call
    def find_object_by(self, obj: IEntry, key, value):
        for k, v in self.Cache.get_items():
            if v[key] == value:
                obj.from_dict(v)
                return obj
        else:
            return None

    def query_string(self, query: str, params: list = None):
        return self.Database.execute(query, params)

