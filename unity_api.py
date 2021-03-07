from flask import Flask,jsonify,request
from Business.unity_server_helper import UnityServerHelper

app=Flask(__name__)

@app.route('/')
def home():
    return "home"

@app.route('/get_data',methods=["POST"])
def get_data():
    result = UnityServerHelper.get_data(request.json)
    return jsonify(result)

@app.route('/run_query',methods=["POST"])
def run_query():
    result = UnityServerHelper.run_query(request.json)
    return jsonify(result)

if __name__ == '__main__':
    app.run()


"""
Post Model:
{
    "server_info":
    {
        "host":"",
        "username":"",
        "password":"",
        "database":""
    },
    "sql_code":""
}
"""
