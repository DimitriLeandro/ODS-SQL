from pyexcel_ods import get_data
import json


sqlCreateDatabase = ""
sqlCreateTable = ""
sqlInsert = ""


def openOdsFile():
    while True:
        fileName = input("Enter file name: ")
        try:
            return json.loads(json.dumps(get_data(fileName)))
        except:
            print("File not found. Please, try again.")


def askDatabaseName():
    dbName = input("Enter database name: ")
    global sqlCreateTable
    sqlCreateTable += "CREATE DATABASE " + dbName + ";\n"
    sqlCreateTable += "USE " + dbName + ";\n\n"


def getTablesName(objJson):
    arrayTables = []
    for table in objJson:
        arrayTables.append(table)
    return arrayTables


def setCreateTable(table):
    global sqlCreateTable
    sqlCreateTable += "CREATE TABLE " + table + " (\n"
    sqlCreateTable += "\tid INT NOT NULL AUTO_INCREMENT,\n"


def closeTableScript(table):
    global sqlCreateTable
    sqlCreateTable += "\tCONSTRAINT pk_" + table + " PRIMARY KEY (id)\n"
    sqlCreateTable += ");\n\n"


def getTableColumns(objJson, table):
    arrayColumns = []
    for field in objJson[table][0]:
        arrayColumns.append(field)
    return arrayColumns


def askColumnType(column, i, length):
    type = input(column + " -> ")
    type = type.upper()
    global sqlCreateTable
    sqlCreateTable += "\t" + column + " " + type
    if i == length:
        sqlCreateTable += "\n"
    else:
        sqlCreateTable += ",\n"


def startInsert(table, arrayColumns):
    global sqlInsert
    sqlInsert += "INSERT INTO " + table + " ("
    p = 0
    for column in arrayColumns:
        p += 1
        if p == len(arrayColumns):
            sqlInsert += column
        else:
            sqlInsert += column + ", "
    sqlInsert += ") VALUES\n"


def insertValues(objJson, table, arrayColumns):
    global sqlInsert
    q = 0
    for row in objJson[table]:
        q += 1
        if q != 1:
            sqlInsert += "("
            j = 0
            for value in row:
                j += 1
                if (j != len(arrayColumns)):
                    sqlInsert += "'" + str(value) + "', "
                else:
                    sqlInsert += "'" + str(value) + "'"
            if j != len(arrayColumns):
                qtLeft = len(arrayColumns) - j
                for k in range(0, qtLeft):
                    if k == qtLeft - 1:
                        sqlInsert += "''"
                    else:
                        sqlInsert += "'',"
            if q == len(objJson[table]):
                sqlInsert += ");\n\n"
            else:
                sqlInsert += "),\n"


# ------STARTING-------
objJson = openOdsFile()
askDatabaseName()
arrayTables = getTablesName(objJson)
# ---FOR EACH TABLE----
for table in arrayTables:
    # -------------------------CREATE TABLE SCRIPT-----------------------------
    setCreateTable(table)
    arrayColumns = getTableColumns(objJson, table)
    print("Set columns type for table " + table + ": (Exemple: VARCHAR(30))")
    i = 0
    for column in arrayColumns:
        i += 1
        askColumnType(column, i, len(arrayColumns))
    closeTableScript(table)
    # -----------------------INSERT VALUES INTO TABLE--------------------------
    startInsert(table, arrayColumns)
    insertValues(objJson, table, arrayColumns)
# ------FINISHING-------
sqlFullScript = sqlCreateDatabase + sqlCreateTable + sqlInsert
print(sqlFullScript)
