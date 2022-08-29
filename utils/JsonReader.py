import json
import os

class JsonReader:

    def readJsonFile(self, fileName):
        print(os.getcwd()+"/testdata/")
        dirPath = os.getcwd()+"/testdata/"
        with open(dirPath+fileName,"r") as readFile:
            jsonStruct = json.load(readFile)
            return jsonStruct

