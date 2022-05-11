
import urllib.request
from urllib.parse import quote
import string
import json
import codecs
import numpy

lonRange = [2.2295347307800224, 2.2615455215567963]  # the range of longitude
latRange = [48.88462128622945, 48.897046503784956]  # the range of latitude

lonDivision = 0.005
latDivision = 0.005
radius = 500
TIMEOUT = 30
outfile = "output.csv"

#   Google Key
googleKey = "AIzaSyBfT1zTN6-ezvwGKrB7P2AaFB870xssvW8"

#restaurant_j = json_format(res_test)
print('start')
print('totally have'+str(((lonRange[1]-lonRange[0])/lonDivision+1)*((latRange[1]-latRange[0])/latDivision+1))+'requests')
count = 0
countLine = 0

place_id_list = []
csvFile=codecs.open(outfile,'a','utf-8')
csvFile.write('lat,lon,types\n')

for lon in numpy.arange(lonRange[0], lonRange[1], lonDivision):
    print('already have'+str(count)+'request，get'+str(countLine)+'information')
    for lat in numpy.arange(latRange[0], latRange[1], latDivision):
        print('already have'+str(count)+'request，get'+str(countLine)+'information')
        #   发请求
        latlon = str(lat)+','+str(lon)
        basic_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={0}&location={1}&radius={2}'
        url = basic_url.format(googleKey,latlon,radius)
        url = quote(url, safe = string.printable)
        req = urllib.request.urlopen(url,timeout=TIMEOUT)
        response = req.read().decode('utf-8')
        responseJSON = json.loads(response)
        for item in responseJSON['results']:
            #对每个POI
            place_id = item['place_id']
            types = item['types']
            #如果id不在已有的list里
            if not place_id in place_id_list:
                #如果类型中有point_of_interest
                if "point_of_interest" in types:
                    place_id_list.append(place_id)
                    line = str(item['geometry']['location']['lat']) + ',' + str(item['geometry']['location']['lng'])
                    for type in types:
                        line = line + ',' + str(type)
                    csvFile.write(line + '\n')
                    countLine = countLine + 1
        count = count + 1
csvFile.close()
print('end')

