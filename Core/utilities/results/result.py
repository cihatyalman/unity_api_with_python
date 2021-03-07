class Result:
    def __init__(self, success:bool, message="Successful"):
        self.success = success
        self.message = message

    def toMap(self):
        map = {}
        map["success"] = self.success
        map["message"] = self.message
        return map
