from Core.utilities.results.result import Result

class DataResult(Result):

    def __init__(self, success:bool, message="Successful", data=None):
        super().__init__(success, message)
        self.data = data

    def toMap(self):
        map = super().toMap()
        map["data"]=self.data
        return map
