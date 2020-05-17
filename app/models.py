from app import utils


class WeatherData(object):
    def __init__(self, location, daily_weather_list):
        self.location = location
        self.daily = daily_weather_list


class DailyWeather:
    def __init__(self, date, weather, temp):
        self.date = date
        self.weather = weather
        self.temp = temp


class Location(object):
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


class WeatherDate:
    def __init__(self, weekday, date):
        self.weekday = weekday
        self.date = date


class WeatherDetails:
    def __init__(self, main, description):
        self.main = main
        self.description = description


class WeatherTemperature:
    def __init__(self, temp, temp_max, temp_min):
        self.temp = temp
        self.temp_max = temp_max
        self.temp_min = temp_min


def get_weather_data(weather_dict):
    location_name = weather_dict['name']
    location_lat = weather_dict['coord']['lat']
    location_lon = weather_dict['coord']['lon']
    location = Location(location_name, location_lat, location_lon)

    date = utils.timestamp_to_datetime(weather_dict['dt'])
    weekday = utils.datetime_to_weekday(date)
    date_str = utils.datetime_to_date_string(date)
    weather_date = WeatherDate(weekday, date_str)

    main = weather_dict['weather'][0]['main']
    description = weather_dict['weather'][0]['description']
    weather_details = WeatherDetails(main, description)

    temp = utils.convert_temp_to_celsius_rounded(weather_dict['main']['temp'])
    temp_min = utils.convert_temp_to_celsius_rounded(weather_dict['main']['temp_min'])
    temp_max = utils.convert_temp_to_celsius_rounded(weather_dict['main']['temp_max'])
    temperature = WeatherTemperature(temp, temp_max, temp_min)

    daily_weather = DailyWeather(weather_date, weather_details, temperature)

    return WeatherData(location, [daily_weather])


def get_daily_weather(weather_dict):
    date = utils.timestamp_to_datetime(weather_dict['dt'])
    weekday = utils.datetime_to_weekday(date)
    date_str = utils.datetime_to_date_string(date)
    weather_date = WeatherDate(weekday, date_str)

    main = weather_dict['weather'][0]['main']
    description = weather_dict['weather'][0]['description']
    weather_details = WeatherDetails(main, description)

    temp = utils.convert_temp_to_celsius_rounded(weather_dict['temp']['day'])
    temp_min = utils.convert_temp_to_celsius_rounded(weather_dict['temp']['min'])
    temp_max = utils.convert_temp_to_celsius_rounded(weather_dict['temp']['max'])
    temperature = WeatherTemperature(temp, temp_max, temp_min)

    return DailyWeather(weather_date, weather_details, temperature)


def dict_to_daily_forecast(weather_dict):
    daily_list = []
    daily = weather_dict['daily']
    for weather in daily:
        daily_weather = get_daily_weather(weather)
        daily_list.append(daily_weather)

    return daily_list


def add_daily_forecast(weather_data, daily_forecast):
    weather_data.daily.extend(daily_forecast)
    return weather_data
