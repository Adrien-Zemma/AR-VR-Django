using UnityEngine;
using UnityEngine.UI;
using SimpleJSON;
using System.Collections;
using UnityEngine.Networking;

public class Camera : MonoBehaviour {
    public Text Box;
    public Text Box2;
    public Text Box3;
    private string username = "adrien";
    private string password = "adrienadrien";
    private string auth;
   
    private void GetBox(string nb, string text)
    {
        switch(nb)
        {
            case ("1"):
                Box.text = text;
                break;
            case ("2"):
                Box2.text = text;
                break;
            case ("3"):
                Box3.text = text;
                break;
        }
    }

    public IEnumerator GetWeather(string nb)
    {
        string url = "http://api.openweathermap.org/data/2.5/weather?q=Lyon&APPID=b52ad82f5e7bbd37afc0abde3712dfc6&units=metric&lang=fr";
        UnityWebRequest www = new UnityWebRequest(url);
        yield return www.SendWebRequest();
        Debug.Log("B");
        var json = JSON.Parse(www.downloadHandler.text);
        GetBox(nb, json.ToString());
    }

    public IEnumerator GetUrls(string url)
    {
        UnityWebRequest www = UnityWebRequest.Get(url);
        www.SetRequestHeader("AUTHORIZATION", auth);
        yield return www.SendWebRequest();
        var json = JSON.Parse(www.downloadHandler.text);
        
        for (int i = 0; json[i] != null; i++)
        {
            Debug.Log("A");
            switch (json[i]["topics"].ToString())
            {
                case "meteo":
                    Debug.Log("B");
                    StartCoroutine(GetWeather(json[i]["numero_case"].ToString()));
                    break;
            }
        }
    }

    private void    MakeAuth()
    {
        auth = username + ":" + password;
        auth = System.Convert.ToBase64String(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(auth));
        auth = "Basic " + auth;
    }

    void Start ()
    {
        MakeAuth();
        StartCoroutine(GetUrls("http://127.0.0.1:8000/api/polls/?format=json"));
    }
    
    void Update ()
    {
    }
}
