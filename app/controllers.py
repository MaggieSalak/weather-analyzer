import os
from dotenv import load_dotenv
from app import models, utils


class WeatherController:

    def __init__(self):
        load_dotenv(os.path.join(os.getcwd(), '.env'))

        self.cityId = os.getenv('CITY_ID')
        self.apiKey = os.getenv('API_KEY')

    def current_weather_url(self):
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        url = base_url + '?id=' + str(self.cityId) + '&appid=' + self.apiKey
        return url

    def get_current_weather(self):
        url = self.current_weather_url()
        weather_dict = utils.query_url(url)
        print(weather_dict)
        weather_data = models.dict_to_weather_data(weather_dict)
        return weather_data
