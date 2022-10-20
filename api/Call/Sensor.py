import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
ContentType = SETTING['API']['ContentType']
SensorAPIPath = SETTING['API']['PATH']['Sensor']
SensorID = SETTING['API']['SensorID']
def data(SK) :
    path = SensorAPIPath+SensorID
    urls = apiUrl + path
    headers = {
        'session': SK,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code

    assetText = response.text
    assetJson = json.loads(assetText)
    assetsDataJson = assetJson['data']
    dataList = assetsDataJson['result_sets'][0]['rows']
    #print(dataList)
    dataListAppend = []
    for j in range(len(dataList)) :
        DL = []
        for k in range(len(dataList[j]['data'])) :
            DL.append(dataList[j]['data'][k][0]['text'])
        dataListAppend.append(DL)
    returnList = {'resCode': resCode, 'dataList': dataListAppend}
    return returnList

