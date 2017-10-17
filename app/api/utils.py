import ast
import json
import csv
from api.objectjson import ObjectJson as objson

def load_json_file(file):
    """load json file and return data_dict
    :param file json file format
    """
    with open(file, "r", encoding="utf-8-sig") as file:
        data_dict = ast.literal_eval(file.read())
        #jsn = json.dumps(data_dict)
    return data_dict

def parse_json(json_data, **required_data):
    extracted_data = {}
    for key, data in required_data.items():
        tmp = json_data
        if ("." in data):
            temp_keys = data.split(".")
            for temp_key in temp_keys:
                tmp = tmp[temp_key]
            extracted_data[key] = tmp
        else:
            extracted_data[key] = json_data[data]
    return extracted_data

def parse_json_dot(json_data, **required_data):
    extracted_data = {}
    j = objson(json_data)
    for key, data in required_data.items():
        extracted_data[key] = getattr(j, data)
    return extracted_data

def read_file(filename, mode, buffer, encoding=None):
    try:
        with open(filename, mode, buffer, encoding) as file:
            return file.read()
    except IOError:
        return "Help file not found"

def convert_tuple_to_list(t, list_=[]):
    for item in t:
        if  isinstance (item, tuple):
            list_ = convert_tuple_to_list(item, list_)
        else:
            list_.append(item)
    return list_

def load_all_cities_from_csv(filename, *colnames):
    cities = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for col in colnames:
                cities.append(row[col])
    return cities

def show_help(filename):
    message = status = ""
    try:
        with open(filename, "r", 624, 'utf-8-sig') as file:
            for line in file.readlines():
                message += f"<p>{line}"
        status = True
    except IOError as e:
        status = False
        message = f"Help not available, please contact admin with details '{e.strerror}'"
    return {"message":message, "status":status}

def show_history(history):
    keys = sorted(history.keys(), reverse=True)
    records = ''
    if (len(history) == 0):
        records = "Not history records are found, please do some search and retry"
    else:
        for key in keys:
            records += f"<p>--------------<b>Record No# {key}:</b>--------------<p>{history.get(key)}"
    return records

def reverse_dict(data_dict):
    reverse_dict = {}
    keys = sorted(data_dict.keys(), reverse=True)
    for key in keys:
        reverse_dict[key] = data_dict.get(key)
    return reverse_dict
