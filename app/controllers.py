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

    def forecast_url(self, weather_data):
        base_url = 'https://api.openweathermap.org/data/2.5/onecall'
        url = base_url + '?lat=' + str(weather_data.location.lat) + \
            '&lon=' + str(weather_data.location.lon) + \
            '&exclude=current,minutely,hourly' + \
            '&appid=' + self.apiKey
        print(url)
        return url

    def get_weather_forecast(self, weather_data):
        url = self.forecast_url(weather_data)
        weather_dict = utils.query_url(url)
        return weather_dict

    def get_weather(self):
        current_weather_dict = self.get_current_weather()
        print(current_weather_dict)
        current_weather = models.dict_to_weather_data(current_weather_dict)
        weather_forecast = self.get_weather_forecast(current_weather)
        print('forecast')
        print(weather_forecast)
        return current_weather
