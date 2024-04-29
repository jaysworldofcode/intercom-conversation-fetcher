import json
import os

def get_json_content(file:str):
        
    with open(file, "r+") as json_file:
        print(json_file.readline())
        # if(len(json_file.read()) == 0):
        #     print('Empty')
        #     return False
        
        # json_data = json.load(json_file)
        # print(json_data)
        # return json.load(json_data)
        
def write_json_data(file:str, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)