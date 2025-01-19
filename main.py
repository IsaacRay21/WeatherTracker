import requests
import datetime

API_KEY = "9Q6UUD35AW3D5853RCSYTFL7T"
UNIT = 'us'
HOME = 'minneapolis'
PARAMS = {'unit-group': UNIT, 'key': API_KEY, 'contentType' : 'json'}

def weeklyForecast(location=HOME):
    start = datetime.date.today()
    end = start + datetime.timedelta(days=7)
    r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start}/{end}", params = PARAMS)
    return r

def dailyForecast(location=HOME):
    today = datetime.date.today()
    r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{today}", params = PARAMS)
    return r

def hourlyForecast(location=HOME):
    now = datetime.datetime.now()
    r = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{now}", params = PARAMS)
    return r