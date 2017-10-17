#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import api.utils as utils

def city_exists(url, city, timeout=15):
    try:
        resp = requests.get(url % city, timeout)
    except requests.exceptions.ConnectionError:
        return False, "Connection failed, please retry later"
    else:
        resp_data = resp.json()
        result = utils.parse_json_dot(resp_data, **{"status":"status","status":"HeWeather5[0].status"})
        if result.get("status") == 'ok':
            return True, "ok"
        else:
            return False, "City doesn't exist"

def retrieve_weather_data_by_city(url, timeout=15, **weather_info):
    result = {}
    status = ""
    try:
        resp = requests.get(url, timeout)
    except ConnectionError:
        result['message'] = ('Connection failed, please retry later')
        status = False
    else:
        resp_data = resp.json()
        print(resp_data)
        result = utils.parse_json_dot(resp_data, **weather_info)
        status = True
    return result, status

def fetch_city_weather(cityname, count):
    city, result = retrieve_weather_data_by_city(
                                cityname, **weather_info)
    if city == cityname:
        city_weather = rh.show_weather(city, result)
        print(f"The current weather for city: \"<b>{cityname}</b>\"<p>{city_weather}")
        history[count] = city_weather
        count += 1
    else:
        print(
        "Not found any command or city that matches, please type 'help' for all commands"
        )
    return count
