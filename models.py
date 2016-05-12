
class Weather:

    def __init__(self, conditions_dict):
        #self.weather is referring to standard "cloudy, overcast, rainy, snowy" etc
        self.weather = conditions_dict["current_observation"]["weather"]
        self.temperature_string = conditions_dict["current_observation"]["temperature_string"]
        self.feelslike_string = conditions_dict["current_observation"]["feelslike_string"]
        self.wind_mph = conditions_dict["current_observation"]["wind_mph"]
        self.pressure_in = conditions_dict["current_observation"]["pressure_in"]
        self.visibility_mi = conditions_dict["current_observation"]["visibility_mi"]
        self.precip_today_in = conditions_dict["current_observation"]["precip_today_in"]
        self.wind_dir = conditions_dict["current_observation"]["wind_dir"]

    def __str__(self):

        return """The weather is {}. The actual temperature is {} degrees, although it feels like {} degrees. \n
                The wind is blowing at {} mph and the air pressure is {}. Visibility is {} miles. \n
                The wind is blowing {}. There has been {} inches of precipitation today.""".format(self.weather,
                self.temperature_string, self.feelslike_string, self.wind_mph, self.pressure_in, self.visibility_mi,
                self.wind_dir, self.precip_today_in)

class Forecast:

    def __init__(self, forecast10day_dict):
        #self.day refers to day 1, day 2, day 3 etc from current day, not day of week
        self.day = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"]
        self.avg_wind = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["avewind"]["mph"]
        self.weekday =  forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["date"]["weekday_short"]
        self.month_name = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["date"]["monthname"]
        self.date_day = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["date"]["day"]
        self.day_low = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["low"]["fahrenheit"]
        self.day_high = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["high"]["fahrenheit"]
        self.weather = forecast10day_dict["forecast"]["simpleforecast"]["forecastday"][self.day]["conditions"]

    def __str__(self):

        return """The forecast for {}, {} {}, is {}. Average windspped will be {}. The high will be {} degrees
        and the low {}.""".format(self.weekday, self.month_name, self.date_day, self.weather, self.avg_wind, self.day_high, self.day_low)

class Sun:

    def __init__(self, astronomy_dict):

        self.rise_min = astronomy_dict["sun_phase"]["sunrise"]["minute"]
        self.rise_hour = astronomy_dict["sun_phase"]["sunrise"]["hour"]
        self.set_min = astronomy_dict["sun_phase"]["sunset"]["minute"]
        self.set_hour = astronomy_dict["sun_phase"]["sunset"]["hour"]

    def __str__(self):

        return "The sun will rise at {}:{} and set at {}:{}.".format(self.rise_hour, self.rise_min, self.set_hour, self.set_min)

class Alert:

    def __init__(self, alerts_dict):

        self.status = alerts_dict["alerts"]

    def __str__(self):

        for item in self.status:
            return "{}".format(item)

    def print_alerts(self):

        if len(self.status) == 0:
            return "There are not currently any weather alerts."
        else:
            for item in self.alerts:
                return "Weather alert: {}".format(item)

class Hurricane:

    def __init__(self, currenthurricane_dict):

        self.status = currenthurricane_dict["currenthurricane"]

    def __str__(self):
        fr item in self.status:
            return "{}".format(item)

    def print_alerts(self):

        if len(self.status) == 0:
            return "There are not currently any hurricane alerts."
        else:
            return "There is currently a hurrican alert in your area."
