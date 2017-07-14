import requests
from bs4 import BeautifulSoup

def weather(cityname):
    cityname=cityname.replace('台','臺')    
    key="{{Your Api Key}}"
    #F-C0032-001 can get city's weather info
    dataid="F-C0032-001"
    api="http://opendata.cwb.gov.tw/opendataapi?dataid="+dataid+"&authorizationkey="+key
    print(api)
    print('Start parsing weather ...')
    rs = requests.session()
    res = rs.get(api, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    dic={}
    i=0
    for city in soup.select('locationname'):
        dic[city.string]=i
        i+=15

    idx=dic[cityname]
    content =""
    wstatus = soup.select('parametername')[idx]
    low_temp = soup.select('parametername')[idx+6]
    high_temp = soup.select('parametername')[idx+3]
    comfor = soup.select('parametername')[idx+9]
    rate = soup.select('parametername')[idx+12]
    
    content += cityname + '\n' + '天氣概況:' + wstatus.string + '\n'
    content += '氣溫:' + low_temp.string + '°C~' + high_temp.string + '°C \n'
    content += '舒適度:' + comfor.string + '\n'
    content += '降雨機率:' + rate.string + '%'    
    return content

weather('台北市')
