from peewee import SqliteDatabase
from configuration.wrappers import singleton

@singleton
class DatabaseProvider:
    _database = SqliteDatabase('db.sqlite3')

    def getDatabase(self):
        return self._database
    
    def setTables(self, *models):
        if not self._database.is_connection_usable():
            self._database.connect()
        self._database.create_tables(models)
