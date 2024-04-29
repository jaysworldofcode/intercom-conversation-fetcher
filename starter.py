from app_state import AppState
import colorama
from colorama import Fore, init
from datetime import datetime
import time
import os
from lib.repository.intercom_conversation import get_conversations
from lib.modules.logger import message_logger, MESSAGE_TYPE
from lib.modules.json import get_json_content, write_json_data

# init panorama
init()

class Starter:

    max_retry = 10
    retries = 0

    def __init__(self):
        #set report path
        AppState.report_path = os.environ.get("GENERATED_REPORT_PATH")+AppState.report_path+'.json'
        print(AppState.report_path)
         
        self.__()
        
    def __(self):
        is_fetching = True

        while is_fetching:
            result = get_conversations(
                per_page=os.environ.get("PER_PAGE"),
                starting_after=AppState.next_page_key,
                token=os.environ.get("AUTHORIZATION_TOKEN"),
                intercom_version=os.environ.get("INTERCOM_VERSION")
            )
            message_logger('status code '+str(result.status_code), MESSAGE_TYPE.SUCCESS)
            
            if(result.status_code != 200):
                self.retries += 1

                #if retry is at max stop the loop                
                if(self.retries > self.max_retry):
                    is_fetching = False
                    message_logger('Max retry complete, stopping the program now', MESSAGE_TYPE.ERROR)
                else:
                    message_logger('Encounter an error while processing request, retry '+str(self.retries)+'x', MESSAGE_TYPE.ERROR)

                continue
                
            result_json_format = result.json()

            if('pages' in result_json_format and 'next' in result_json_format['pages'] and 'starting_after' in result_json_format['pages']['next']):
                message_logger('Found next starting key: '+result_json_format['pages']['next']['starting_after'], MESSAGE_TYPE.MESSAGE)
                AppState.next_page_key = result_json_format['pages']['next']['starting_after']
            else:
                message_logger('No next starting_after key found, stopping the program now', MESSAGE_TYPE.ERROR)
                is_fetching = False

            AppState.conversations = AppState.conversations+result_json_format['conversations']
            message_logger('Total Messages: '+str(len(AppState.conversations)), MESSAGE_TYPE.MESSAGE)

            write_json_data(
                AppState.report_path,
                AppState.conversations
            )

            message_logger('Message successfully save', MESSAGE_TYPE.SUCCESS)

            self.retries = 0