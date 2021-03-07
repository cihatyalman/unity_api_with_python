using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class UnityApi : MonoBehaviour
{
    string _baseLink = "unity_api_link";

    private void Start()
    {
        string serverInfo = @"{"host":"","username":"","password":"","database":""}"
		string sqlCode="SELECT * FROM demo";
        string webApiRequest = @"{"server_info":{+},"sql_code":{*}}".Replace("{+}",serverInfo).Replace("{*}",sqlCode)

        //StartCoroutine(GetRequest("/"));
        //StartCoroutine(PostRequestJson("/get_data", webApiRequest));
        //StartCoroutine(PostRequestForm("/get_data"));
    }

    private void PathValidation(string path)
    {
        if (!path.StartsWith("/")) throw new Exception(message: @"The path must start with ""/""");
    }

    IEnumerator GetRequest(string path)
    {
        PathValidation(path);

        UnityWebRequest www = UnityWebRequest.Get(_baseLink+path);
        yield return www.SendWebRequest();

        if (www.isNetworkError) 
        { 
            Debug.Log("Error While Sending: " + www.error); 
        }
        else 
        { 
            Debug.Log("Result: " + www.downloadHandler.text); 
        }
    }
    	
    IEnumerator PostRequestJson(string path, string jsonData)
    {
        PathValidation(path);
        // print(jsonData);

        UnityWebRequest www = UnityWebRequest.Post(_baseLink+path, jsonData);
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(jsonData);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        yield return www.SendWebRequest();

        if (www.isNetworkError) 
        { 
            Debug.Log("Error While Sending: " + www.error); 
        }
        else
        {
            Debug.Log("Result: " + www.downloadHandler.text);
            // string result = www.downloadHandler.text;
            // Result resultObject = new Result();
            // JsonUtility.FromJsonOverwrite(result, resultObject);
            // print(JsonUtility.ToJson(resultObject));
        }
    }
	
    IEnumerator PostRequestForm(string path)
    {
        PathValidation(path);

        WWWForm form = new WWWForm();
        form.AddField("server_info", "info");
        form.AddField("sql_code", "code");

        UnityWebRequest www = UnityWebRequest.Post(_baseLink+path, form);
        yield return www.SendWebRequest();

        if (www.isNetworkError) 
        { 
            Debug.Log("Error While Sending: " + www.error); 
        }
        else
        {
            Debug.Log("Result: " + www.downloadHandler.text);
            string result = www.downloadHandler.text;
            Result resultObject = new Result();
            JsonUtility.FromJsonOverwrite(result, resultObject);
            print(JsonUtility.ToJson(resultObject));
        }
    }

    [Serializable]
    public class DataResult
    {
        public bool success;
        public string message;
        public List data;
    }

    [Serializable]
    public class Result
    {
        public bool success;
        public string message;
    }

}

#region Sample Queries
/*
string createTable = "CREATE TABLE demo(id INT(10) UNSIGNED PRIMARY KEY NOT NULL,username VARCHAR(50) NOT NULL)";
string deleteTable = "DROP TABLE demo";
string getAllFromTable = "SELECT * FROM demo";
string insertToTable = @"INSERT INTO demo VALUES (1,""user1""),(2,""user2"")";
string deleteValueFromTable = "DELETE FROM demo WHERE id=1 or id=2";
string updateValueFromTable = @"UPDATE demo SET username=""newUser"" WHERE id=2";
*/
#endregion
