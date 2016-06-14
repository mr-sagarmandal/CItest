#!/usr/bin/env python
from urllib2 import urlopen
from contextlib import closing
import json

# Automatically geolocate the connecting IP
#url = 'http://freegeoip.net/json/'
url= 'http://ip-api.com/json'
try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
        print(location)
        location_city = location['city']
        location_state = location['region_name']
        location_country = location['country_name']
        location_zip = location['zipcode']
        url2= 'api.openweathermap.org/data/2.5/weather?lat=%&lon=%&APPID=c3dae359f90443db69dd233e25b9875d' %(location['lat'], location['lon'])
        print(url2)
except:
    print("Location could not be determined automatically")
