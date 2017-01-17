import requests
import json
import time

headers = {'User-Agent': 'My User Agent 1.0',}


api_url = "https://api.flightradar24.com/common/v1/flight/list.json?query=%s&fetchBy=reg&page=1&limit=100&token="

names = open('plane_names.txt','r')
result_file = open('result.csv','w+')

result_file.write("Flight Number,callsign,codeshare,diverted,utc,local,Aircraft Type,Aircraft subtype,hex,registration,serialNo,owner,Airline Name,Airline IATA Code,Airline ICAO Code,Airport Name,Airport IATA,Airport ICAO,Country Name,Country Code,City,Time Zone City,UTC Offset,Time Zone Abbreviation,Time Zone Name,Airport Name,Airport IATA,Airport ICAO,Dest Country Name,Dest Country Code,Destination City Name,Time Zone City,UTC Offset,Time Zone Abbreviation,Time Zone Name,Scheduled Dept,Scheduled Arr,Real Dept,Real Arr,Est Dept,Est Arr,Updated")

for name in names:
    name = name.replace('\n','').replace(' ','')
    result = requests.get(api_url % (name),headers=headers)
    print(result.status_code)
    result = result.text
    result = json.loads(result)
        
    for data in result['result']['response']['data']:
        try:
            
            w = []
            print (data['aircraft']['owner'])
            w.append(str(data['identification']['number']['default']))
            w.append(str(data['identification']['callsign']))
            w.append(str(data['identification']['codeshare']))
            w.append(str(data['status']['generic']['status']['diverted']))
            w.append(str(data['status']['generic']['eventTime']['utc']))
            w.append(str(data['status']['generic']['eventTime']['local']))
            w.append(str(data['aircraft']['model']['code']))
            w.append(str(data['aircraft']['model']['text']))
            w.append(str(data['aircraft']['hex']))
            w.append(str(data['aircraft']['registration']))
            w.append(str(data['aircraft']['serialNo']))
            w.append(str(data['aircraft']['owner']))
            w.append(str(data['airline']['name']))
            w.append(str(data['airline']['code']['iata']))
            w.append(str(data['airline']['code']['icao']))
            w.append(str(data['airport']['origin']['name']))
            w.append(str(data['airport']['origin']['code']['iata']))
            w.append(str(data['airport']['origin']['code']['icao']))
            w.append(str(data['airport']['origin']['position']['country']['name']))
            w.append(str(data['airport']['origin']['position']['country']['code']))
            w.append(str(data['airport']['origin']['position']['region']['city']))
            w.append(str(data['airport']['origin']['timezone']['name']))
            w.append(str(data['airport']['origin']['timezone']['offset']))
            w.append(str(data['airport']['origin']['timezone']['abbr']))
            w.append(str(data['airport']['origin']['timezone']['abbrName']))
            w.append(str(data['airport']['destination']['name']))
            w.append(str(data['airport']['destination']['code']['iata']))
            w.append(str(data['airport']['destination']['code']['icao']))
            w.append(str(data['airport']['destination']['position']['country']['name']))
            w.append(str(data['airport']['destination']['position']['country']['code']))
            w.append(str(data['airport']['destination']['position']['region']['city']))
            w.append(str(data['airport']['destination']['timezone']['name']))
            w.append(str(data['airport']['destination']['timezone']['offset']))
            w.append(str(data['airport']['destination']['timezone']['abbr']))
            w.append(str(data['airport']['destination']['timezone']['abbrName']))
            w.append(str(data['time']['scheduled']['departure']))
            w.append(str(data['time']['scheduled']['arrival']))
            w.append(str(data['time']['real']['departure']))
            w.append(str(data['time']['real']['arrival']))
            w.append(str(data['time']['estimated']['departure']))
            w.append(str(data['time']['estimated']['arrival']))
            w.append(str(data['time']['other']['updated']))
            # x_ = ','.join(w)
            # print x_
            result_file.write('\n'+str(','.join(w)))
        except:
            pass
            # print 'got error for ',str(data).encode('utf-8')

    time.sleep(5)