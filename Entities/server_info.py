class ServerInfo:
    def __init__(self,host="",username="",password="",database=""):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def toMap(self):
        map = {}
        map["host"] = self.host
        map["username"] = self.username
        map["password"] = self.password
        map["database"] = self.database
        return map
