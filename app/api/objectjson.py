"""
Inspired by Author in [Objectjson - JSON to nested object. - Python - Snipplr Social Snippet Repository](http://snipplr.com/view/71218/objectjson--json-to-nested-object/)
https://ideone.com/O6KGB3
Modified by Vwan - Add handling for key passed as concated string like "test.a"
"""
import json
import sys
import random
import string

class ObjectJson(object):
    def __init__(self, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        self.json_data = json_data

    def parse_squared_key(self, key):
        start_loc = key.index("[")
        index = int(key[start_loc+1:-1])
        return key[0:start_loc],index

    def __getitem__(self, index):
        return ObjectJson(self.json_data[index])

    def __getattr__(self, key):
        if "." in key:
            data = self.json_data
            key = key.split(".")
            for k in key:
                if "[" in k:
                    left, index = self.parse_squared_key(k)
                    if left in data:
                        if isinstance(data[left][index], (list, dict)):
                            data = data[left][index]
                        else:
                            self.json_data = self.json_data[left]
                    else:
                        raise Exception('There is no json_data[\'{key}\'].'.format(key=k))
                else:
                    # print("data is:", data)
                    data = data[k]
            return data
        else:
            if key in self.json_data:
                if isinstance(self.json_data[key], (list, dict)):
                    return ObjectJson(self.json_data[key])
                else:
                    return self.json_data[key]
            else:
                raise Exception('There is no json_data[\'{key}\'].'.format(key=key))


    def __repr__(self):
        out = self.__dict__
        return '%r' % (out['json_data'])

if __name__ == '__main__':
    str2 = '{"HeWeather5":[{"basic":{"city":"北京","cnty":"中国","id":"CN101010100","lat":"39.90498734","lon":"116.40528870","update":{"loc":"2017-08-26 17:46","utc":"2017-08-26 09:46"}},"daily_forecast":[{"astro":{"mr":"10:02","ms":"21:36","sr":"05:37","ss":"18:55"},"cond":{"code_d":"100","code_n":"300","txt_d":"晴","txt_n":"阵雨"},"date":"2017-08-26","hum":"25","pcpn":"0.0","pop":"0","pres":"1016","tmp":{"max":"29","min":"18"},"uv":"7","vis":"16","wind":{"deg":"0","dir":"无持续风向","sc":"微风","spd":"6"}},{"astro":{"mr":"11:01","ms":"22:08","sr":"05:38","ss":"18:54"},"cond":{"code_d":"306","code_n":"300","txt_d":"中雨","txt_n":"阵雨"},"date":"2017-08-27","hum":"64","pcpn":"12.7","pop":"100","pres":"1014","tmp":{"max":"22","min":"18"},"uv":"2","vis":"14","wind":{"deg":"0","dir":"无持续风向","sc":"微风","spd":"6"}},{"astro":{"mr":"11:59","ms":"22:42","sr":"05:39","ss":"18:52"},"cond":{"code_d":"104","code_n":"100","txt_d":"阴","txt_n":"晴"},"date":"2017-08-28","hum":"44","pcpn":"0.0","pop":"71","pres":"1015","tmp":{"max":"28","min":"18"},"uv":"5","vis":"18","wind":{"deg":"0","dir":"无持续风向","sc":"微风","spd":"6"}}],"status":"ok"}]}'
    j = ObjectJson(str2)
    fs = [
    #'HeWeather5[0].basic.city',
    'HeWeather5[0].daily_forecast[%d].date',
    'HeWeather5[0].daily_forecast[%d].cond.txt_n'
    ]

    print("+++", j.HeWeather5[0].daily_forecast[0].date) # ok
    print("+++", getattr(j, 'HeWeather5[0].daily_forecast[0].date'))

    for f in fs:
        print("--fs---",f)
        for i in range(3):
            print(i)
            if("%d" in f):
                fn = f % i
                value = getattr(j, fn)
                print(f"{fn}: {value}")
