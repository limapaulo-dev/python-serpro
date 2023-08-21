import sqlite3

class DAO:
    _dbTableName = "tableName"

    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def getConn(self):
         return self._conn

    def selectAll(self):
        if (self._dbTableName != "tableName"):
            return self._conn.execute(f"SELECT * FROM {self._dbTableName}")
        else:
            print("error: call selectAll in the respective class")
      
    def selectById(self, id):
        if (self._dbTableName != "tableName"): 
            return self._conn.execute(f"SELECT * FROM {self._dbTableName} WHERE id = ?", (id,)) 
        else:
            print("error: call selectById in the respective class")           
        
    def deleteById(self, id):
        if (self._dbTableName != "tableName"):
            self._conn.execute(f"DELETE FROM {self._dbTableName} WHERE id = ?", (id,))
            print(f"{self._dbTableName.capitalize()} deletado com sucesso.")
        else:
            print("error: call deleteById in the respective class")  
    