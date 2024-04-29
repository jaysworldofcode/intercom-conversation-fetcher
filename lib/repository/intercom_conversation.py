import requests
import os


def get_conversations(per_page:int, starting_after:str, token:str, intercom_version:str):
    url = os.environ.get("APP_URL")+'conversations'
    query = {
        'per_page': per_page
    }
    headers = {
        "Intercom-Version": intercom_version,
        'Authorization': 'Bearer '+token
    }
    
    if(starting_after != None):
        query['starting_after'] = starting_after
    
    response = requests.get(url, headers=headers, params=query)
    
    return response
