from Entities.server_info import ServerInfo

class Query():
    def __init__(self,server_info:dict, sql_code=""):
        self.server_info = ServerInfo(server_info["host"],server_info["username"],server_info["password"],server_info["database"])
        self.sql_code = sql_code

    def toMap(self):
        map = super().toMap()
        map["sql_code"] = self.sql_code
        return map
