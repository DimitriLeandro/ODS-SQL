from pyexcel_ods import get_data
import json
import os
import getpass


class FileHandler():

    def openOdsFile(self):
        while True:
            fileName = input("Enter path and ODS filename (Exemple: /home/" + getpass.getuser() + "/Documents/sheet.ods): ")
            try:
                return json.loads(json.dumps(get_data("../../.." + fileName)))
            except:
                print("File not found. Please, try again.")


    def verifyCurrentDirectory(self):
        if os.getcwd() != "/opt/ODS-SQL/Core":
            print("You must copy ODS-SQL folder to /opt/")
            return False
        else:
            return True


    def createSQLFile(self, script, dbName):
        try:
            objFile = open("../../../home/" + getpass.getuser() + "/" + dbName + ".sql", 'w')
            objFile.write(script)
            print("Document saved in: /home/" + getpass.getuser() + "/" + dbName + ".sql")
            objFile.close()
        except:
            print("Error trying to create /home/" + getpass.getuser() + "/" + dbName + ".sql")