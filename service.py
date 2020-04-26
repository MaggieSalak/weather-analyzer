import os
import requests
from dotenv import load_dotenv

class WeatherService:

    def __init__(self):
        load_dotenv(os.path.join(os.getcwd(), '.env'))

        self.cityId = 2657896
        self.apiKey = os.getenv("API_KEY")

    def get_url(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        url = base_url + "?id=" + str(self.cityId) + "&appid=" + self.apiKey
        print(url)
        return url

    def get_current_weather(self):
        r = requests.get(url=self.get_url())
        data = r.json()
        return str(data)
