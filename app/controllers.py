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
        return weather_dict

    def past_weather_url(self):
        base_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
        url = base_url + '?id=' + str(self.cityId) + '&appid=' + self.apiKey
        print(url)
        return url

    def get_weather(self):
        current_weather_dict = self.get_current_weather()
        print(current_weather_dict)
        current_weather_data = models.dict_to_weather_data(current_weather_dict)
        return current_weather_data
