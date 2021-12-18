import json

def read_json_data(filename):
    '''
    Our input is going to be in the JSON format so we will be using the json package to load the data
    '''
    raw_data = None
    with open(filename) as json_file:
        raw_data = json.load(json_file)
    return raw_data

