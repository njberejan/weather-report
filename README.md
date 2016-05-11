key: 96fd72e23c579a3a

from https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1:

import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/96fd72e23c579a3a/geolookup/conditions/q/IA/Cedar_Rapids.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()

GET http://api.wunderground.com/api/96fd72e23c579a3a/features/settings/q/query.format

features: conditions
          forecast10day
          astronomy
          alerts
          currenthurricane

settings: lang:EN

query: [6 digit zip code]

format: json
