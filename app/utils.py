import calendar
import json
import requests
from datetime import datetime
from scipy.constants import convert_temperature


def query_url(url):
    print('Querying URL')
    resp = requests.get(url=url)
    resp_json = json.dumps(resp.json())
    return json.loads(resp_json)


def convert_temp_to_celsius_rounded(temp_kelvin):
    temp_celsius = convert_temperature(temp_kelvin, 'K', 'C')
    return int(temp_celsius.round())


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def datetime_to_weekday(date):
    return calendar.day_name[date.weekday()]


def day_number_suffix(day_num):
    if day_num % 10 == 1 and day_num != 11:
        return 'st'
    if day_num % 10 == 2 and day_num != 12:
        return 'nd'
    if day_num % 10 == 3 and day_num != 13:
        return 'rd'
    return 'th'

def datetime_to_date_string(date):
    day_suffix = day_number_suffix(date.day)
    month_str = date.strftime('%B')
    return month_str + ' ' + str(date.day) + day_suffix
