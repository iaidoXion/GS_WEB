import requests
import json



with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
SesstionKeyPath = APISETTING['API']['PATH']['SesstionKey']
ID = APISETTING['API']['username']
PWD = APISETTING['API']['password']



def SessionKey():
    try:
        path = SesstionKeyPath
        urls = apiUrl+path
        headers = '{"username" : "'+ID+'","domain":"",  "password":"'+PWD+'"}'
        response = requests.post(urls, data=headers, verify=False)
        #response = requests.request("POST", urls, data=headers, verify=False)
        a = response.json()
        resCode = response.status_code
        sessionKey = a['data']['session']

        returnList = sessionKey

        return returnList
    except ConnectionError as e:
        print(e)
