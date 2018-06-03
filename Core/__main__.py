from SQLWriter import SQLWriter
from FileHandler import FileHandler
import os

#Instance new objects
objFileHandler = FileHandler()
objSQLWriter = SQLWriter()
# ------STARTING-------
if(objFileHandler.verifyCurrentDirectory()):
    objJson = objFileHandler.openOdsFile()
    objSQLWriter.askDatabaseName()
    arrayTables = objSQLWriter.getTablesName(objJson)
    # ---FOR EACH TABLE----
    for table in arrayTables:
        # -------------------------CREATE TABLE SCRIPT-----------------------------
        objSQLWriter.setCreateTable(table)
        arrayColumns = objSQLWriter.getTableColumns(objJson, table)
        print("Set columns type for table " + table + ": (Exemple: VARCHAR(30))")
        i = 0
        for column in arrayColumns:
            i += 1
            objSQLWriter.askColumnType(column, len(arrayColumns))
        objSQLWriter.closeTableScript(table)
        # -----------------------INSERT VALUES INTO TABLE--------------------------
        objSQLWriter.startInsert(table, arrayColumns)
        objSQLWriter.insertValues(objJson, table, arrayColumns)
    # ------FINISHING-------
    objFileHandler.createSQLFile(objSQLWriter.getFullSQLScript(), objSQLWriter.getDBName())
    print("\n\n\n" + objSQLWriter.getFullSQLScript())
