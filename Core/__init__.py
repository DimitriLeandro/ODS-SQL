from pyexcel_ods import get_data
from SQLWriter import SQLWriter
import json


def openOdsFile():
    while True:
        fileName = input("Enter file name: ")
        try:
            return json.loads(json.dumps(get_data(fileName)))
        except:
            print("File not found. Please, try again.")


# ------STARTING-------
objJson = openOdsFile()
objSQLWriter = SQLWriter()
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
objFile = open('sql.txt','w')
objFile.write(objSQLWriter.getFullSQLScript())
objFile.close()
print(objSQLWriter.getFullSQLScript())
