from Core.utilities.results.data_result import DataResult

class SuccessDataResult(DataResult):

    def __init__(self, message="Successful", data=None):
        super().__init__(True, message, data)
