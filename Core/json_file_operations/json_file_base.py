import json
import os

class JsonFileBase:
    def __init__(self,path:str):
        "path: file path must end with (.json, .txt, .data, .cybox)"
        assert(path.endswith(".json") or path.endswith(".txt") or path.endswith(".data") or path.endswith(".cybox"))
        self.path = path

    def write(self,json_list:dict):
        assert(type(json_list) is dict)
        with open(self.path,"w") as file:
            json.dump(json_list,file)

    def read(self):
        "return value is dict"
        with open(self.path,"r") as file:
            return json.load(file)

    def delete(self):
        os.remove(self.path)

"""
json.loads(string)      : string -> json
json.dumps(json)        : json -> string

json.load(file)         : file -> json
json.dump(json,file)    : json -> file
"""
