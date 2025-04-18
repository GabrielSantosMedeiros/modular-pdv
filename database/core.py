from peewee import SqliteDatabase
from configuration.wrappers import Singleton
from configuration.settings import BASE_DIR

@Singleton
class DatabaseProvider:
    _database = SqliteDatabase(BASE_DIR / 'db.sqlite3')

    def getDatabase(self):
        return self._database
    
    def setTables(self, *models):
        if not self._database.is_connection_usable():
            self._database.connect()
        self._database.create_tables(models)
