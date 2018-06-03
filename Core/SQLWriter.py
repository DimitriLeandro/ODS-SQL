class SQLWriter():
    def __init__(self):
        self.sqlCreateDatabase = ""
        self.sqlCreateTable = ""
        self.sqlInsert = ""
        self.dbName = ""

    def askDatabaseName(self):
        self.dbName = input("Enter database name: ")
        self.sqlCreateTable += "CREATE DATABASE " + self.dbName + ";\n"
        self.sqlCreateTable += "USE " + self.dbName + ";\n\n"


    def getTablesName(self, objJson):
        arrayTables = []
        for table in objJson:
            arrayTables.append(table)
        return arrayTables

    def setCreateTable(self, table):
        self.sqlCreateTable += "CREATE TABLE " + table + " (\n"
        self.sqlCreateTable += "\tid INT NOT NULL AUTO_INCREMENT,\n"

    def closeTableScript(self, table):
        self.sqlCreateTable += "\tCONSTRAINT pk_" + table + " PRIMARY KEY (id)\n"
        self.sqlCreateTable += ");\n\n"

    def getTableColumns(self, objJson, table):
        arrayColumns = []
        for field in objJson[table][0]:
            arrayColumns.append(field)
        return arrayColumns

    def askColumnType(self, column, length):
        type = input(column + " -> ")
        type = type.upper()
        self.sqlCreateTable += "\t" + column + " " + type
        self.sqlCreateTable += ",\n"

    def startInsert(self, table, arrayColumns):
        self.sqlInsert += "INSERT INTO " + table + " ("
        p = 0
        for column in arrayColumns:
            p += 1
            if p == len(arrayColumns):
                self.sqlInsert += column
            else:
                self.sqlInsert += column + ", "
        self.sqlInsert += ") VALUES\n"

    def insertValues(self, objJson, table, arrayColumns):
        q = 0
        for row in objJson[table]:
            q += 1
            if q != 1:
                self.sqlInsert += "("
                j = 0
                for value in row:
                    j += 1
                    if (j != len(arrayColumns)):
                        self.sqlInsert += "'" + str(value) + "', "
                    else:
                        self.sqlInsert += "'" + str(value) + "'"
                if j != len(arrayColumns):
                    qtLeft = len(arrayColumns) - j
                    for k in range(0, qtLeft):
                        if k == qtLeft - 1:
                            self.sqlInsert += "''"
                        else:
                            self.sqlInsert += "'',"
                if q == len(objJson[table]):
                    self.sqlInsert += ");\n\n"
                else:
                    self.sqlInsert += "),\n"

    def getFullSQLScript(self):
        return (self.sqlCreateDatabase + self.sqlCreateTable + self.sqlInsert)

    def getDBName(self):
        return self.dbName