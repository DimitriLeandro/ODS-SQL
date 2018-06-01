from pyexcel_ods import get_data
import json


def openOdsFile():
    while True:
        fileName = input("File name: ")
        try:
            return json.loads(json.dumps(get_data(fileName)))
        except:
            print("File not found. Please, try again.\n")


def getTablesName(objJson):
    arrayTables = []
    for table in objJson:
        arrayTables.append(table)
    return arrayTables


def getTableColumns(objJson, table):
    arrayColumns = []
    for field in objJson[table][0]:
        arrayColumns.append(field)
    return arrayColumns


objJson = openOdsFile()
arrayTables = getTablesName(objJson)
for table in arrayTables:
    arrayColumns = getTableColumns(objJson, table)
    print(len(arrayColumns))

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
