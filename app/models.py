from scipy.constants import convert_temperature


class WeatherData(object):
    def __init__(self, location, weather, temp):
        self.location = location
        self.weather = weather
        self.temp = temp


class Location(object):
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


class WeatherDetails:
    def __init__(self, main, description):
        self.main = main
        self.description = description


class WeatherTemperature:
    def __init__(self, temp, temp_max, temp_min):
        self.temp = temp
        self.temp_max = temp_max
        self.temp_min = temp_min


def convert_temp_to_celsius_rounded(temp_kelvin):
    temp_celsius = convert_temperature(temp_kelvin, 'K', 'C')
    return int(temp_celsius.round())


def dict_to_weather_data(weather_dict):
    location_name = weather_dict['name']
    location_lat = weather_dict['coord']['lat']
    location_lon = weather_dict['coord']['lon']
    location = Location(location_name, location_lat, location_lon)

    main = weather_dict['weather'][0]['main']
    description = weather_dict['weather'][0]['description']
    weather_details = WeatherDetails(main, description)

    temp = convert_temp_to_celsius_rounded(weather_dict['main']['temp'])
    temp_min = convert_temp_to_celsius_rounded(weather_dict['main']['temp_min'])
    temp_max = convert_temp_to_celsius_rounded(weather_dict['main']['temp_max'])
    temperature = WeatherTemperature(temp, temp_max, temp_min)

    return WeatherData(location, weather_details, temperature)
