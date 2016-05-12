

class Weather:

    def __init__(self):
        #self.weather is referring to standard "cloudy, overcast, rainy, snowy" etc
        self.weather = "current_observation.weather": "Overcast"
        self.temperature_string = "current_observation.temperature_string": "78.3 F (25.7 C)"
        self.feelslike_string = "current_observation.feelslike_string": "81 F (27 C)"
        self.wind_mph = "current_observation.wind_mph": 0
        self.pressure_in = "current_observation.pressure_in": "30.07"
        self.visibility_mi = "current_observation.visibility_mi": "10.0"
        self.precip_today_in = "current_observation.precip_today_in": "0.21"
        self.wind_dir = "current_observation.wind_dir": "SW"

    def __str__(self):

        return """The weather is {}. The actual temperature is {} degrees, although it feels like {} degrees. \n
                The wind is blowing at {} mph and the air pressure is {}. Visibility is {} miles. \n
                The wind is blowing {}. There has been {} inches of precipitation today.""".format(self.weather,
                self.temperature_string, self.feelslike_string, self.wind_mph, self.pressure_in, self.visibility_mi,
                self.wind_dir, self.precip_today_in)

class Forecast:

    def __init__(self):
        #self.day refers to day 1, day 2, day 3 etc from current day, not day of week
        self.day = "forecast.simpleforecast.forecastday.1
        self.avg_wind = "forecast.simpleforecast.forecastday.1.avewind.mph": 4
        self.weekday =  "forecast.simpleforecast.forecastday.1.date.weekday_short": "Thu"
        self.month_name = "forecast.simpleforecast.forecastday.1.date.monthname": "May"
        self.date_day = "forecast.simpleforecast.forecastday.1.date.day": 12
        self.day_low = "forecast.simpleforecast.forecastday.1.low.fahrenheit": "65"
        self.day_high = "forecast.simpleforecast.forecastday.1.high.fahrenheit": "83"
        self.weather = "forecast.simpleforecast.forecastday.1.conditions": "Overcast"

    def __str__(self):

        return """The forecast for {}, {} {}, is {}. Average windspped will be {}. The high will be {} degrees
        and the low {}.""".format(self.weekday, self.month_name, self.date_day, self.weather, self.avg_wind, self.day_high, self.day_low)

class Sun:

    def __init__(self):

        self.rise_min = "sun_phase.sunrise.minute": "13",
        self.rise_hour = "sun_phase.sunrise.hour": "6",
        self.set_min = "sun_phase.sunset.minute": "11",
        self.set_hour = "sun_phase.sunset.hour": "20"

    def __str__(self):

        return "The sun will rise at {}:{} and set at {}:{}.".format(self.rise_hour, self.rise_min, self.set_hour, self.set_min)

class Alert:

    def __init__(self):

        self.status = "alerts": []

    def __str__(self):

        fr item in self.status:
            return "{}".format(item)

    def print_alerts(self):

        if len(self.status) == 0:
            return "There are not currently any weather alerts."
        else:
            for item in self.alerts:
                return "Weather alert: {}".format(item)

class Hurricane:

    def __init__(self):

        self.status = "currenthurricane": []

    def __str__(self):
        fr item in self.status:
            return "{}".format(item)

    def print_alerts(self):

        if len(self.status) == 0:
            return "There are not currently any hurricane alerts."
        else:
            return "There is currently a hurrican alert in your area."
