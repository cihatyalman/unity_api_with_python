from Core.utilities.results.result import Result

class SuccessResult(Result):
    def __init__(self, message="Successful"):
        super().__init__(True, message)
        