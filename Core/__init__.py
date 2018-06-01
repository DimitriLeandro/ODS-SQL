from pyexcel_ods import get_data
import json

sqlScript = ""


def openOdsFile():
    while True:
        fileName = input("Enter file name: ")
        try:
            return json.loads(json.dumps(get_data(fileName)))
        except:
            print("File not found. Please, try again.")


def askDatabaseName():
    dbName = input("Enter database name: ")
    global sqlScript
    sqlScript += "CREATE DATABASE " + dbName + ";\n"
    sqlScript += "USE " + dbName + ";\n\n"


def getTablesName(objJson):
    arrayTables = []
    for table in objJson:
        arrayTables.append(table)
    return arrayTables


def setCreateTable(table):
    global sqlScript
    sqlScript += "CREATE TABLE " + table + " (\n"
    sqlScript += "\tid INT NOT NULL AUTO_INCREMENT,\n"


def closeTableScript(table):
    global sqlScript
    sqlScript += "\tCONSTRAINT pk_" + table + " PRIMARY KEY (id)\n"
    sqlScript += ");\n\n"


def getTableColumns(objJson, table):
    arrayColumns = []
    for field in objJson[table][0]:
        arrayColumns.append(field)
    return arrayColumns


def askColumnType(column, i, length):
    type = input(column + " -> ")
    type = type.upper()
    global sqlScript
    sqlScript += "\t" + column + " " + type
    if i == length:
        sqlScript += "\n"
    else:
        sqlScript += ",\n"


objJson = openOdsFile()
askDatabaseName()
arrayTables = getTablesName(objJson)
for table in arrayTables:
    setCreateTable(table)
    arrayColumns = getTableColumns(objJson, table)
    print("Set columns type for table " + table + ": (Exemple: VARCHAR(30))")
    i = 0
    for column in arrayColumns:
        i += 1
        askColumnType(column, i, len(arrayColumns))
    closeTableScript(table)
print(sqlScript)

'''
for linha in objJson['Sheet1']: #para cada linha dessa: ['Jõao Nascimento', 13, 'Mas'] no objJson...
    insertRow = "("
    contador = 0
    for metaDado in linha: #para cada metadado na linha do json...
        contador += 1
        if(contador != 3):
            insertRow += "'" + str(metaDado) + "', "
        else:
            insertRow += "'" + str(metaDado) + "'"
    if(contador == 0):
        insertRow += "'', '', ''),"
    elif(contador == 1):
        insertRow += "'', ''),"
    elif(contador == 2):
        insertRow += "''),"
    else:
        insertRow += "),"
    print(insertRow)
'''
