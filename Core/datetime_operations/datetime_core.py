from datetime import datetime,timedelta

class DateTimeCore:

    @staticmethod
    def get_timestamp(gmt:int=0):
        "Return timestamp as string"
        timestamp = datetime.timestamp(datetime.now()+timedelta(hours=gmt))
        return str(int(timestamp))

    @staticmethod
    def to_datetime(my_timestamp:str):
        "Return datetime as datetime"
        return datetime.fromtimestamp(float(my_timestamp))

    @staticmethod
    def to_timestamp(my_datetime:datetime):
        "Return timestamp as string"
        return str(int(datetime.timestamp(my_datetime)))
