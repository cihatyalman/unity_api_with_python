from Core.utilities.results.data_result import DataResult

class ErrorDataResult(DataResult):

    def __init__(self, message="ERROR", data=None):
        super().__init__(False, message, data)
