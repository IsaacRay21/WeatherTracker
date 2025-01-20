import requests
import datetime

class WeatherData:
    def __init__(self):
        self.API_KEY = "9Q6UUD35AW3D5853RCSYTFL7T"
        self.UNIT = 'us'
        self.HOME = 'minneapolis'
        self.PARAMS = {'unit-group': self.UNIT, 'key': self.API_KEY, 'contentType' : 'json'}

    def weeklyForecast(self):
        start = datetime.date.today()
        end = start + datetime.timedelta(days=7)
        r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}/{}".format(self.HOME, start, end), params = self.PARAMS)
        return r.json()

    def dailyForecast(self):
        today = datetime.date.today()
        r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}".format(self.HOME, today), params = self.PARAMS)
        return r.json()

    def hourlyForecast(self):
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}".format(self.HOME,  now), params = self.PARAMS)
        return r.json()



