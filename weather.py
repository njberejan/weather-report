"""API KEY: 96fd72e23c579a3a"""

"""Step 1: locate API links DONE: SEE README"""
"""Step 2: write responses to files for testing"""
"""Step 3: write code to extract info based on location"""

"""last thing to do is hook up code to API directly"""
#needs to query MULTIPLE API endpoints
#needs to present a weather summary to the user based on location (via zipcode)
#summary prints to console, must include:
## current conditions
## 10 day forecast
## sunrise/sunset times
## current weather alerts
## list of all active hurricanes (anywhere)

#code must be written in classes and spread across multiple files
## bryce suggests one class per API endpoints

#for testing purposes, write data from API to files (if you ping the API too many times, will lose access to their servers)

import requests
import json

"""the below writes conditions API to text file."""
# url = 'http://api.wunderground.com/api/96fd72e23c579a3a/geolookup/conditions/q/27707.json'
# f = open('test_data.txt', 'w')
# response = requests.get(url=url)
# data = response.json()
# for key, value in (data['current_observation']).items():
#     string = (str(key) + ' : ' + str(value) + '\n')
#     f.write(string)

"""the below converts conditions API to JSON format and writes to JSON file."""
# with open('conditions_test.json', 'w') as f:
#     data = data[string]
#     json.dump(data, f)

conditions = 'http://api.wunderground.com/api/96fd72e23c579a3a/conditions/lang:EN/q/27707.json'
forecast10day = 'http://api.wunderground.com/api/96fd72e23c579a3a/forecast10day/lang:EN/q/27707.json'
astronomy = 'http://api.wunderground.com/api/96fd72e23c579a3a/astronomy/lang:EN/q/27707.json'
alerts = 'http://api.wunderground.com/api/96fd72e23c579a3a/alerts/lang:EN/q/27707.json'
currenthurricane = 'http://api.wunderground.com/api/96fd72e23c579a3a/currenthurricane/lang:EN/q/27707.json'


def make_json_test(filename, string):
    response = requests.get(url=string)
    data = response.json()
    with open(filename, 'w') as f:
        json.dump(data, f)

filename_list = ['conditions_test.json', 'forecast10day.json', 'astronomy.json', 'alerts.json', 'currenthurricane.json']
string_list = [conditions, forecast10day, astronomy, alerts, currenthurricane]
for filename, item in zip(filename_list, string_list):
    make_json_test(filename, item)
