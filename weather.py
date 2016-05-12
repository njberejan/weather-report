import requests
import json
from models import Weather, Forecast, Sun, Alert, Hurricane


def main():

    zipcode = input("Please enter a zipcode to see the weather report: ")

    conditions = 'http://api.wunderground.com/api/96fd72e23c579a3a/conditions/lang:EN/q/' + zipcode + '.json'
    forecast10day = 'http://api.wunderground.com/api/96fd72e23c579a3a/forecast10day/lang:EN/q/' + zipcode + '.json'
    astronomy = 'http://api.wunderground.com/api/96fd72e23c579a3a/astronomy/lang:EN/q/' + zipcode + '.json'
    alerts = 'http://api.wunderground.com/api/96fd72e23c579a3a/alerts/lang:EN/q/' + zipcode + '.json'
    currenthurricane = 'http://api.wunderground.com/api/96fd72e23c579a3a/currenthurricane/lang:EN/q/' + zipcode + '.json'

# """code for creating JSON test files:"""
# def make_json_test(filename, string):
#     response = requests.get(url=string)
#     data = response.json()
#     with open(filename, 'w') as f:
#         json.dump(data, f)

# filename_list = ['conditions_test.json', 'forecast10day.json', 'astronomy.json', 'alerts.json', 'currenthurricane.json']
# string_list = [conditions, forecast10day, astronomy, alerts, currenthurricane]
# for filename, item in zip(filename_list, string_list):
#     make_json_test(filename, item)

    response1 = requests.get(url=conditions)
    conditions_dict = response1.json()

    response2 = requests.get(url=forecast10day)
    forecast10day_dict = response2.json()

    response3 = requests.get(url=astronomy)
    astronomy_dict = response3.json()

    response4 = requests.get(url=alerts)
    alerts_dict = response4.json()

    response5 = requests.get(url=currenthurricane)
    currenthurricane_dict = response5.json()

    weather = Weather(conditions_dict)
    print(weather)
    #below forecast code does not work, returns "TypeError: 'str' object is not callable"
    # for day in forecast10day_dict["forecast"]["simpleforecast"]["forecastday"]:
    #     forecast = forecast10day(forecast10day_dict)
    #     print(forecast)
    sun = Sun(astronomy_dict)
    print(sun)
    alerts = Alert(alerts_dict)
    print(alerts.print_alerts())
    hurricane = Hurricane(currenthurricane_dict)
    print(hurricane.print_alerts())

main()
