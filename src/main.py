from pyexcel_ods import get_data
import json

objJson = json.loads(json.dumps(get_data("planilha.ods")))
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