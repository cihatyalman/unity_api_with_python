import pymysql
from Entities.server_info import ServerInfo
from Entities.query import Query

from Core.utilities.results.success_data_result import SuccessDataResult
from Core.utilities.results.error_data_result import ErrorDataResult
from Core.utilities.results.success_result import SuccessResult
from Core.utilities.results.error_result import ErrorResult

class UnityServerHelper:

    @classmethod
    def __db_connect(cls,server_info:ServerInfo):
        con = pymysql.connect(host=server_info.host,user=server_info.username,
        passwd=server_info.password,db=server_info.database)
        return con

    @classmethod
    def get_data(cls,query:str):
        try:
            q = Query(query["server_info"],query["sql_code"])
            con = cls.__db_connect(q.server_info)
            cur = con.cursor()
            cur.execute(q.sql_code)
            # get keys
            db_keys = [x[0] for x in cur.description]
            #get value
            db_values = cur.fetchall()
            result_json = []
    
            for value in db_values:
                result_json.append(dict(zip(db_keys, value)))
            cur.close()
            con.close()
    
            result = SuccessDataResult(result_json)
        except:
            result = ErrorDataResult("Query Error !")
        finally:
            return result.toMap()
    

    @classmethod
    def run_query(cls,query:str):
        try:
            q = Query(query["server_info"],query["sql_code"])
            con = cls.__db_connect(q.server_info)
            cur = con.cursor()
            cur.execute(q.sql_code)
            con.commit()
            cur.close()
            con.close()
            result = SuccessResult()
        except:
            result = ErrorResult("Query Error !")
        finally:
            return result.toMap()


#region Sample Queries 
# Auto increment if "AUTO_INCREMENT" is added
create_table="CREATE TABLE demo(id INT(10) UNSIGNED PRIMARY KEY NOT NULL ,username VARCHAR(50) NOT NULL)"
delete_table="DROP TABLE demo"
get_all_from_table="SELECT * FROM demo"
insert_to_table="INSERT INTO demo VALUES (1,'user1'),(2,'user2')"
delete_value_from_table="DELETE FROM demo WHERE id=1 or id=2"
update_value_from_table="UPDATE demo SET username='new_user' WHERE id=2"
#endregion
