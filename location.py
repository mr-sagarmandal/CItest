#!/usr/bin/env python
from urllib2 import urlopen
from contextlib import closing
import json

# Automatically geolocate the connecting IP
#url = 'http://freegeoip.net/json/'
url= 'http://ip-api.com/json'
response= urlopen(url)
location = json.loads(response.read())
#print(location)
location_city = location['city']
location_zip = location['zip']
url2= 'http://api.openweathermap.org/data/2.5/weather?lat=%7.4f&lon=%7.4f&APPID=c3dae359f90443db69dd233e25b9875d' %(location['lat'], location['lon'])
sunny= urlopen(url2)
weather= json.loads(sunny.read())
print(weather)
