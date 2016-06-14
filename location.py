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
except:
    print("Location could not be determined automatically")
