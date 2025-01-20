from gui import MyGUI
from data import WeatherData

class WeatherApp():
    def __init__(self, update_interval=3600000):
        self.gui = MyGUI()
        self.data = WeatherData()
        self.update_interval = update_interval

    def update(self):
        forecast = self.data.dailyForecast()
        todayCast = forecast['days'][0]

        currTemp = todayCast['temp']
        self.gui.currTemp.config(text="Temperature: {}".format(currTemp))

        currHigh = todayCast['tempmax']
        self.gui.currHigh.config(text="High: {}".format(currHigh))

        currLow = todayCast['tempmin']
        self.gui.currLow.config(text="Low: {}".format(currLow))


        self.scheduleUpdate()

    def scheduleUpdate(self):
        self.gui.root.after(self.update_interval, self.update)
    
    def run(self):
        self.update()
        self.gui.run()

if __name__ == "__main__":
    app = WeatherApp()
    app.run()