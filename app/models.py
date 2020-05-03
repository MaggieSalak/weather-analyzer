from scipy.constants import convert_temperature

class WeatherData(object):
    def __init__(self, location, weather, description, temp, temp_min, temp_max):
        self.location = location
        self.weather = weather
        self.description = description
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max


def convert_temp_to_celsius_rounded(temp_kelvin):
    temp_celsius = convert_temperature(temp_kelvin, 'K', 'C')
    return temp_celsius.round()

def dict_to_weather_data(weather_dict):
    location = weather_dict['name']
    weather = weather_dict['weather'][0]['main']
    description = weather_dict['weather'][0]['description']
    temp = convert_temp_to_celsius_rounded(weather_dict['main']['temp'])
    temp_min = convert_temp_to_celsius_rounded(weather_dict['main']['temp_min'])
    temp_max = convert_temp_to_celsius_rounded(weather_dict['main']['temp_max'])

    return WeatherData(location, weather, description, temp, temp_min, temp_max)